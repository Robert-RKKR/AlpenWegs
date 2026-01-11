//  Imports:
import { Box, Burger, Button, Center, Collapse, Divider, Drawer, useMantineTheme,
  HoverCard, ScrollArea, UnstyledButton, Group, Text } from "@mantine/core";
import { IconChevronDown, IconTrekking } from "@tabler/icons-react";
import { planningMenu, trackingMenu } from "./pageHeaderData";
import { PageHeaderDropdown } from "./PageHeaderDropdown";
import { useAuthStore } from "../../../stores/authStore";
import { NavLink, Link } from "react-router-dom";
import { UserMenu } from "../userMenu/UserMenu";
import { useDisclosure } from "@mantine/hooks";
import classes from "./PageHeader.module.css";

export function PageHeader() {

  // State for mobile drawer:
  const [drawerOpened, { toggle: toggleDrawer, close: closeDrawer }] = useDisclosure(false);

  // State for dropdown menus:
  const [planningOpened, { toggle: togglePlanning }] = useDisclosure(false);
  const [trackingOpened, { toggle: toggleTracking }] = useDisclosure(false);

  // Handlers authentication state:
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated);

  // Style theme:
  const theme = useMantineTheme();

  return (
    <Box>
      {/* --- Header bar (inside AppShell.Header) --- */}
      <header className={classes.header}>
        <Group justify="space-between" h="100%">
          {/* Logo */}
          <UnstyledButton component={Link} to="/" aria-label="Go to explorer">
            <IconTrekking size={32} color={theme.colors.blue[6]} />
          </UnstyledButton>

          {/* ====== Desktop main navigation ====== */}
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
                <PageHeaderDropdown config={planningMenu} />
              </HoverCard.Dropdown>
            </HoverCard>

            <HoverCard width={600} position="bottom" radius="md" shadow="md" withinPortal>
              <HoverCard.Target>
                <NavLink to="/explorer/track" className={classes.link}>
                  <Center inline>
                    <Box component="span" mr={5}>
                      Tracking
                    </Box>
                    <IconChevronDown size={16} />
                  </Center>
                </NavLink>
              </HoverCard.Target>
              <HoverCard.Dropdown style={{ overflow: "hidden" }}>
                <PageHeaderDropdown config={trackingMenu} />
              </HoverCard.Dropdown>
            </HoverCard>

            <NavLink to="/compendium" className={classes.link}>
              Compendium
            </NavLink>
          </Group>

          {/* --- Desktop Authentication --- */}
          <Group visibleFrom="sm">
            {!isAuthenticated && (
              <>
                <Button variant="default" component={Link} to="/auth/login">
                  Log in
                </Button>
                <Button component={Link} to="/auth/register">
                  Sign up
                </Button>
              </>
            )}
            {isAuthenticated && <UserMenu />}
          </Group>

          {/* Mobile burger */}
          <Burger opened={drawerOpened} onClick={toggleDrawer} hiddenFrom="sm" />
        </Group>
      </header>

      {/* ====== Mobile drawer ====== */}
      <Drawer opened={drawerOpened} onClose={closeDrawer} size="100%" padding="md" title="Navigation" hiddenFrom="sm" zIndex={1000000}>
        <ScrollArea h="calc(100vh - 80px)" mx="-md">
          <Divider my="sm" />

          {/* --- Mobile main navigation --- */}
          <NavLink to="/" className={classes.link} onClick={closeDrawer}>
            <Center w="100%"><Text size="lg">Home</Text></Center>
          </NavLink>

          <UnstyledButton className={classes.link} onClick={togglePlanning}>
            <Center w="100%">
              <Group gap={6}>
                <Box component="span"><Text size="lg">Planning</Text></Box>
                <IconChevronDown size={16} />
              </Group>
            </Center>
          </UnstyledButton>

          <Collapse in={planningOpened}>
            <PageHeaderDropdown config={planningMenu} onItemClick={closeDrawer} mobile={true} />
          </Collapse>

          <UnstyledButton className={classes.link} onClick={toggleTracking}>
            <Center w="100%">
              <Group gap={6}>
                <Box component="span"><Text size="lg">Tracking</Text></Box>
                <IconChevronDown size={16} />
              </Group>
            </Center>
          </UnstyledButton>

          <Collapse in={trackingOpened} mb="lg">
            <PageHeaderDropdown config={trackingMenu} onItemClick={closeDrawer} mobile={true} />
          </Collapse>

          <NavLink to="/compendium" className={classes.link} onClick={closeDrawer}>
            <Center w="100%"><Text size="lg">Compendium</Text></Center>
          </NavLink>

          <Divider my="sm" />

          {/* --- Mobile Authentication --- */}
          <Group justify="center" grow pb="xl" px="md">
            {!isAuthenticated && (
              <>
                <Button variant="default" component={Link} to="/auth/login">
                  Log in
                </Button>
                <Button component={Link} to="/auth/register">
                  Sign up
                </Button>
              </>
            )}
            {isAuthenticated && <UserMenu />}
          </Group>
        </ScrollArea>
      </Drawer>
    </Box>
  );
}
