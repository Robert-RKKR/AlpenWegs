// Imports:

import { primaryFeatures, platformHighlights } from './homePageData';
import {  Button, Grid, SimpleGrid, Text, ThemeIcon, Title, Container,
  Group, Badge, Card, useMantineTheme } from '@mantine/core';
import classes from './HomePage.module.css';
import { Link } from 'react-router-dom';

// HomePage component:
export function HomePage() {
  const theme = useMantineTheme();

  /* --- Primary features --- */
  const primaryFeatureItems = primaryFeatures.map((feature) => (
    <div key={feature.title}>
      <ThemeIcon size={44} component={Link} to={feature.to} radius="md" variant="gradient" gradient={{ deg: 133, from: "blue", to: "cyan" }}>
        <feature.icon size={26} stroke={1.5} />
      </ThemeIcon>

      <Text fz="lg" mt="sm" fw={500}>
        {feature.title}
      </Text>

      <Text c="dimmed" fz="sm">
        {feature.description}
      </Text>
    </div>
  ));

  /* --- Platform highlights --- */
  const platformHighlightCards = platformHighlights.map((item) => (
    <Card key={item.title} component={Link} to={item.to} shadow="md" radius="md" className={classes.card} padding="xl">
      <item.icon size={50} stroke={1.5} color={theme.colors.blue[6]} />

      <Text fz="lg" fw={500} className={classes.cardTitle} mt="md">
        {item.title}
      </Text>

      <Text fz="sm" c="dimmed" mt="sm">
        {item.description}
      </Text>
    </Card>
  ));

  return (
    <div className={classes.wrapper}>
      {/* --- Hero + primary navigation --- */}
      <Container size="xl" py="xl">
        <Grid gutter={80} align="center">
          <Grid.Col span={{ base: 12, md: 5 }}>
            <Title className={classes.title} order={2}>
              Plan, explore, and remember your alpine adventures
            </Title>

            <Text c="dimmed">
              AlpenWegs supports every stage of your outdoor journey – from
              planning routes and preparing for the conditions, through
              real-time navigation, to recording experiences and tracking
              long-term goals across Switzerland’s mountains.
            </Text>

            <Button variant="gradient" component={Link} to="/explorer" gradient={{ deg: 133, from: "blue", to: "cyan" }} size="lg" radius="md" mt="xl"> Get started
            </Button>
          </Grid.Col>

          <Grid.Col span={{ base: 12, md: 7 }}>
            <SimpleGrid cols={{ base: 1, md: 2 }} spacing={30}>
              {primaryFeatureItems}
            </SimpleGrid>
          </Grid.Col>
        </Grid>
      </Container>

      {/* --- Platform highlights --- */}
      <Container size="lg" py="xl">
        <Group justify="center">
          <Badge variant="filled" size="lg">
            Designed for long-term outdoor journeys
          </Badge>
        </Group>

        <Title order={2} className={classes.title} ta="center" mt="sm">
          Built with purpose, not just features
        </Title>

        <Text c="dimmed" className={classes.description} ta="center" mt="md">
          AlpenWeg is shaped around real alpine use cases — from geography-first
          design to long-term progress tracking — supporting meaningful outdoor
          experiences rather than isolated activities.
        </Text>

        <SimpleGrid cols={{ base: 1, md: 3 }} spacing="xl" mt={50}>
          {platformHighlightCards}
        </SimpleGrid>
      </Container>
    </div>
  );
}
