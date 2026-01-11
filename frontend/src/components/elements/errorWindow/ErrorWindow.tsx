// Imports:
import { Center, Stack, Title, Text } from "@mantine/core";
import { IconAlertTriangle } from "@tabler/icons-react";
import type { TablerIcon } from "@tabler/icons-react";

// Types:
type ErrorProps = {
  icon?: TablerIcon;
  title: string;
  description?: string;
  iconSize?: number;
  iconColor?: string;
};

// Component:
export function ErrorWindow({
  icon: Icon = IconAlertTriangle,
  title,
  description,
  iconSize = 96,
  iconColor = "var(--mantine-color-red-6)",
}: ErrorProps) {
  return (
    <Center py="xl">
      <Stack align="center" gap="xs">
        <Icon size={iconSize} color={iconColor} stroke={1.5} />

        <Title order={3} ta="center">
          {title}
        </Title>

        {description && (
          <Text c="dimmed" ta="center">
            {description}
          </Text>
        )}
      </Stack>
    </Center>
  );
}
