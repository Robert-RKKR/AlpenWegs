import { Menu, Button, Avatar, Group, Text } from "@mantine/core";
import { logout } from "../../../modules/profiles/api/authApi";
import { IconLogout, IconUser } from "@tabler/icons-react";
import { useNavigate, NavLink } from "react-router-dom";
import { useAuthStore } from "../../../stores/authStore";

export function UserMenu() {
  const navigate = useNavigate();

  const { user, refreshToken, clearAuth } = useAuthStore();

  async function handleLogout() {
    try {
      if (refreshToken) {
        await logout(refreshToken);
      }
    } finally {
      clearAuth();
      navigate("/auth/login");
    }
  }

  return (
    <Menu shadow="md" width={220} position="bottom-end">
      <Menu.Target>
        <Button variant="subtle" px="xs">
          <Group gap="xs">
            <Avatar radius="xl" size={28}>
              <IconUser size={16} />
            </Avatar>
            <Text size="sm" fw={500}>
              {user?.first_name}
            </Text>
          </Group>
        </Button>
      </Menu.Target>

      <Menu.Dropdown>
        <Menu.Label>
          {user?.first_name} {user?.last_name}
        </Menu.Label>

        <Menu.Item
          component={NavLink}
          to="/auth/profile"
          leftSection={<IconUser size={16} />}
        >
          Profile
        </Menu.Item>

        <Menu.Divider />

        <Menu.Item
          color="red"
          leftSection={<IconLogout size={16} />}
          onClick={handleLogout}
        >
          Log out
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}
