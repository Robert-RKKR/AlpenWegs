// Mantine imports:
import {
  Button,
  Group,
  Text,
  Card,
  Image,
  Badge,
  Grid,
} from "@mantine/core";
import { IconTrendingUp, IconEye, IconTrekking, IconRoute, IconStars } from '@tabler/icons-react';

// HomePage component:
export function HomePage() {

  return (
    <div style={{ display: "flex", flexDirection: "column" , gap: "20px", padding: "20px" }}>

      <Grid>
        <Grid.Col span={3}>
          <Card shadow="sm" padding="md" radius="md" withBorder>
              
            <Card.Section>
              <Image
                src="https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-8.png"
                height={160}
                alt="Norway"
              />
            </Card.Section>

            <Group justify="space-between" mt="md" mb="xs">
              <Text fw={500}>Lavaux Vineyard Sunset Walk</Text>
              <Badge color="pink" radius="sm" leftSection={<IconTrekking size={14} />}>Hiking</Badge>
            </Group>

            <Group justify="left" gap="md" mb="md">
              <Badge variant="light" color="blue" radius="sm" leftSection={<IconStars size={14} />}>T3</Badge>
              <Badge variant="light" color="blue" radius="sm" leftSection={<IconTrendingUp size={14} />}>1345 m</Badge>
              <Badge variant="light" color="blue" radius="sm" leftSection={<IconRoute size={14} />}>34.5 Km</Badge>
            </Group>

            <Text size="sm" c="dimmed" mb="xs">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </Text>

            <Group justify="center" gap="md" mb="md">
              <Badge variant="outline" color="gray" radius="sm">T3</Badge>
              <Badge variant="outline" color="gray" radius="sm">1345 m</Badge>
              <Badge variant="outline" color="gray" radius="sm">34.5 Km</Badge>
            </Group>

            <Button color="blue" fullWidth radius="md" leftSection={<IconEye size={14} />}>
              Read more about this hike
            </Button>
          </Card>
        </Grid.Col>
      </Grid>

    </div>
  );
}
