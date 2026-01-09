// React / state:
import { useAuthStore } from "../../../../stores/authStore";
import { useQuery } from "@tanstack/react-query";

// API:
import { fetchUserProfile } from "../../api/userApi";
import type { UserModel } from "../../api/userApi";

// Mantine:
import {
  Container,
  Paper,
  Title,
  Text,
  Group,
  Stack,
  Divider,
  Center,
  Loader,
} from "@mantine/core";

export function UserPage() {
  const user = useAuthStore((s) => s.user);

  // Auth guard
  if (!user?.pk) {
    return (
      <Center py="xl">
        <Text c="dimmed">Not authenticated</Text>
      </Center>
    );
  }

  const { data, isLoading, error } = useQuery<UserModel>({
    queryKey: ["user-profile", user.pk],
    queryFn: () => fetchUserProfile(user.pk),
  });

  if (isLoading) {
    return (
      <Center py="xl">
        <Loader />
      </Center>
    );
  }

  if (error || !data) {
    return (
      <Center py="xl">
        <Text c="red">Failed to load profile</Text>
      </Center>
    );
  }

  return (
    <Container size="sm" py="xl">
      <Paper withBorder shadow="sm" radius="md" p="lg">
        {/* Header */}
        <Group mb="md">
          <Title order={3}>User Profile</Title>
        </Group>

        <Divider mb="md" />

        {/* Profile details */}
        <Stack gap="sm">
          <ProfileRow label="ID" value={data.pk} />
          <ProfileRow label="Email" value={data.email} />
          <ProfileRow label="First name" value={data.first_name} />
          <ProfileRow label="Last name" value={data.last_name} />
          <ProfileRow
            label="Phone number"
            value={data.phone_number || "No phone number data"}
          />
          <ProfileRow
            label="Birthday"
            value={data.birthday || "No birthday data"}
          />
          <ProfileRow label="User created" value={data.created} />
          <ProfileRow label="Last login" value={data.last_login} />
        </Stack>
      </Paper>
    </Container>
  );
}

/* Small helper component */
function ProfileRow({
  label,
  value,
}: {
  label: string;
  value: string | number;
}) {
  return (
    <Group justify="space-between" align="flex-start">
      <Text size="sm" c="dimmed">
        {label}
      </Text>
      <Text size="sm" fw={500}>
        {value}
      </Text>
    </Group>
  );
}
