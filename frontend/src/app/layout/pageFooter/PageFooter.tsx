// Imports:
import { IconBrandInstagram, IconBrandTwitter, IconBrandYoutube } from '@tabler/icons-react';
import { ActionIcon, Anchor, Group, Box, Center } from '@mantine/core';
import classes from "./PageFooter.module.css";

const links = [
  { link: '#', label: 'Contact' },
  { link: '#', label: 'Privacy' },
  { link: '#', label: 'Blog' },
  { link: '#', label: 'Store' },
  { link: '#', label: 'Careers' },
];

export function PageFooter() {
  const items = links.map((link) => (
    <Anchor c="dimmed" key={link.label} href={link.link} lh={1} onClick={(event) => event.preventDefault()} size="sm">
      {link.label}
    </Anchor>
  ));

  return (
    <Box h={40} px="sm" className={classes.footer}>
      <Center h="100%">
        <Group gap="md">
          
          {/* Text links */}
          <Group gap="sm">
            { items}
          </Group>

          {/* Social icons */}
          <Group gap={4}>
            <ActionIcon size={22} variant="subtle" radius="xl">
              <IconBrandTwitter size={14} />
            </ActionIcon>
            <ActionIcon size={22} variant="subtle" radius="xl">
              <IconBrandYoutube size={14} />
            </ActionIcon>
            <ActionIcon size={22} variant="subtle" radius="xl">
              <IconBrandInstagram size={14} />
            </ActionIcon>
          </Group>
        </Group>
      </Center>
    </Box>
  );
}
