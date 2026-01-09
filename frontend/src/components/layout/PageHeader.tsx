//  Imports:
import {
  IconBook, IconChartPie3, IconChevronDown, IconTrekking,
  IconCode, IconCoin, IconFingerprint, IconNotification,
} from "@tabler/icons-react";
import {
  Anchor, Box, Burger, Button, Center, Collapse, Divider,
  Drawer, Group, HoverCard, ScrollArea, SimpleGrid,
  Text, ThemeIcon, UnstyledButton, useMantineTheme
} from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { NavLink, Link } from "react-router-dom";

// Import CSS module:
import classes from "./PageHeader.module.css";

/* ------------------------------------------------------------------ */
/* Dropdown feature items (used in desktop hover + mobile collapse)   */
/* ------------------------------------------------------------------ */
const featureLinks = [
  {
    icon: IconCode,
    title: "Open source",
    description: "This Pokémon’s cry is very loud and distracting",
    to: "/features/open-source",
  },
  {
    icon: IconCoin,
    title: "Free for everyone",
    description: "The fluid of Smeargle’s tail secretions changes",
    to: "/features/free",
  },
  {
    icon: IconBook,
    title: "Documentation",
    description: "Yanma is capable of seeing 360 degrees without",
    to: "/features/documentation",
  },
  {
    icon: IconFingerprint,
    title: "Security",
    description: "The shell’s rounded shape and the grooves on its",
    to: "/features/security",
  },
  {
    icon: IconChartPie3,
    title: "Analytics",
    description: "This Pokémon uses its flying ability to quickly chase",
    to: "/features/analytics",
  },
  {
    icon: IconNotification,
    title: "Notifications",
    description: "Combusken battles with the intensely hot flames it spews",
    to: "/features/notifications",
  },
];

export function PageHeader() {
  const theme = useMantineTheme();

  const [drawerOpened, { toggle: toggleDrawer, close: closeDrawer }] =
    useDisclosure(false);
  const [featuresOpened, { toggle: toggleFeatures }] =
    useDisclosure(false);

  /* ------------------------------------------------------------------ */
  /* Feature grid (desktop + mobile)                                     */
  /* ------------------------------------------------------------------ */
  const featureItems = featureLinks.map((item) => (
    <UnstyledButton key={item.title} className={classes.subLink} component={NavLink} to={item.to} onClick={closeDrawer}>
      <Group wrap="nowrap" align="flex-start">
        <ThemeIcon size={34} variant="default" radius="md">
          <item.icon size={22} color={theme.colors.blue[6]} />
        </ThemeIcon>
        <div>
          <Text size="sm" fw={500}>
            {item.title}
          </Text>
          <Text size="xs" c="dimmed">
            {item.description}
          </Text>
        </div>
      </Group>
    </UnstyledButton>
  ));

  return (
    <Box>
      {/* =============================================================== */}
      {/* Header bar (inside AppShell.Header)                             */}
      {/* =============================================================== */}
      <header className={classes.header}>
        <Group justify="space-between" h="100%">
          {/* Logo */}
          <IconTrekking size={32} color={theme.colors.blue[6]} />

          {/* ----------------------------------------------------------- */}
          {/* Desktop navigation                                          */}
          {/* ----------------------------------------------------------- */}
          <Group h="100%" gap={0} visibleFrom="sm">
            <NavLink to="/" className={classes.link}>
              Home
            </NavLink>

            <HoverCard width={600} position="bottom" radius="md" shadow="md" withinPortal>
              <HoverCard.Target>
                <NavLink to="/plans" className={classes.link}>
                  <Center inline>
                    <Box component="span" mr={5}>
                      Planning
                    </Box>
                    <IconChevronDown size={16} />
                  </Center>
                </NavLink>
              </HoverCard.Target>

              <HoverCard.Dropdown style={{ overflow: "hidden" }}>
                <Group justify="space-between" px="md">
                  <Text fw={500}>Features</Text>
                  <Anchor component={NavLink} to="/features" fz="xs">
                    View all
                  </Anchor>
                </Group>

                <Divider my="sm" />

                <SimpleGrid cols={2} spacing={0}>
                  {featureItems}
                </SimpleGrid>

                <div className={classes.dropdownFooter}>
                  <Group justify="space-between">
                    <div>
                      <Text fw={500} fz="sm">
                        Get started
                      </Text>
                      <Text size="xs" c="dimmed">
                        Start planning your next adventure
                      </Text>
                    </div>
                    <Button variant="default">Get started</Button>
                  </Group>
                </div>
              </HoverCard.Dropdown>
            </HoverCard>

            <NavLink to="/explorer/track" className={classes.link}>
              Tracking
            </NavLink>

            <NavLink to="/compendium" className={classes.link}>
              Compendium
            </NavLink>
          </Group>

          {/* Desktop auth */}
          <Group visibleFrom="sm">
            <Button variant="default" component={Link} to="/auth/login">
              Log in
            </Button>
            <Button component={Link} to="/auth/register">
              Sign up
            </Button>
          </Group>

          {/* Mobile burger */}
          <Burger opened={drawerOpened} onClick={toggleDrawer} hiddenFrom="sm" />
        </Group>
      </header>

      {/* =============================================================== */}
      {/* Mobile drawer                                                   */}
      {/* =============================================================== */}
      <Drawer opened={drawerOpened} onClose={closeDrawer} size="100%" padding="md" title="Navigation" hiddenFrom="sm" zIndex={1000000}>
        <ScrollArea h="calc(100vh - 80px)" mx="-md">
          <Divider my="sm" />

          {/* ---------------- Centered main navigation ---------------- */}
          <NavLink to="/" className={classes.link} onClick={closeDrawer}>
            <Center w="100%">Home</Center>
          </NavLink>

          <UnstyledButton className={classes.link} onClick={toggleFeatures}>
            <Center w="100%">
              <Group gap={6}>
                <Box component="span">Planning</Box>
                <IconChevronDown size={16} />
              </Group>
            </Center>
          </UnstyledButton>

          <Collapse in={featuresOpened}>{featureItems}</Collapse>

          <NavLink to="/explorer/track" className={classes.link} onClick={closeDrawer}>
            <Center w="100%">Tracking</Center>
          </NavLink>

          <NavLink to="/compendium" className={classes.link} onClick={closeDrawer}>
            <Center w="100%">Compendium</Center>
          </NavLink>

          <Divider my="sm" />

          {/* ---------------- Auth buttons ---------------- */}
          <Group justify="center" grow pb="xl" px="md">
            <Button variant="default" component={Link} to="/auth/login" onClick={closeDrawer}>
              Log in
            </Button>

            <Button component={Link} to="/auth/register" onClick={closeDrawer}>
              Sign up
            </Button>
          </Group>
        </ScrollArea>
      </Drawer>
    </Box>
  );
}
