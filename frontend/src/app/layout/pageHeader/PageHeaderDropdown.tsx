//  Imports:
import { Anchor, Box, Burger, Button, Center, Collapse, Divider,
  Drawer, Group, HoverCard, ScrollArea, SimpleGrid, Text, ThemeIcon,
  UnstyledButton, useMantineTheme } from "@mantine/core";
import { NavLink } from "react-router-dom";
import classes from "./PageHeader.module.css";

// Types (optional but recommended)
export type DropdownConfig = {
  label: string;
  viewAll: {
    label: string;
    to: string;
  };
  items: {
    icon: any;
    title: string;
    description: string;
    to: string;
  }[];
  footer: {
    title: string;
    description: string;
    button: {
      label: string;
      to: string;
    };
  };
};

type Props = {
  config: DropdownConfig;
  onItemClick?: () => void;
  mobile?: boolean;
};

export function PageHeaderDropdown({ config, onItemClick, mobile }: Props) {

  // Style theme:
  const theme = useMantineTheme();

  return (
    <>
      <Group justify="space-between" px={mobile ? "md" : undefined}>
        <Text fw={500} fz={mobile ? "md" : "sm"}>{config.label}</Text>
        <Anchor component={NavLink} to={config.viewAll.to} fz="xs">
          {config.viewAll.label}
        </Anchor>
      </Group>

      <Divider my="sm" />

      <SimpleGrid cols={2} spacing={0}>
        {config.items.map((item) => (
          <UnstyledButton key={item.title} className={classes.subLink} component={NavLink} to={item.to} onClick={onItemClick}>
            <Group wrap="nowrap" align="flex-start" m={mobile ? "md" : undefined}>
              <ThemeIcon size={34} variant="default" radius="md">
                <item.icon size={22} color={theme.colors.blue[6]} />
              </ThemeIcon>
              <div>
                <Text size={mobile ? "md" : "sm"} fw={500}>
                  {item.title}
                </Text>
                <Text size={mobile ? "sm" : "xs"} c="dimmed">
                  {item.description}
                </Text>
              </div>
            </Group>
          </UnstyledButton>
        ))}
      </SimpleGrid>

      <div className={classes.dropdownFooter}>
        <Group justify="space-between">
          <div>
            <Text fw={500} fz="sm">
              {config.footer.title}
            </Text>
            <Text size="xs" c="dimmed">
              {config.footer.description}
            </Text>
          </div>
          <Button variant="default" component={NavLink} to={config.footer.button.to}>
            {config.footer.button.label}
          </Button>
        </Group>
      </div>
    </>
  );
}
