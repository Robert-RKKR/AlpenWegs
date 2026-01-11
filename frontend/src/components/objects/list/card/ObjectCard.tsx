// Imports:
import { ImageLoader } from "../../../elements/imageLoader/ImageLoader";
import { Card, Text, Group, Badge, Button, Spoiler } from "@mantine/core";
import type { ObjectCardProps } from "../../types";
import { IconEye } from "@tabler/icons-react";
import { Link } from "react-router-dom";

// ObjectCard component:
export function ObjectCard({
  href,
  image,
  title,
  properties = [],
  description,
  extras = [],
}: ObjectCardProps) {
  return (
    <Card shadow="sm" radius="md" withBorder padding="md" style={{ height: "100%" }}>
      {/* Image */}
      <Card.Section>
        <ImageLoader src={image as string} alt={title} height={160}/>
      </Card.Section>

      {/* Title */}
      <Text fw={500} mt="md" mb="xs">
        {title}
      </Text>

      {/* Properties (primary badges) */}
      {properties.length > 0 && (
        <Group gap="xs" mb="sm">
          {properties.map((value, index) => (
            <Badge key={index} variant="light" color="blue" radius="sm">
              {value}
            </Badge>
          ))}
        </Group>
      )}

      {/* Description */}
      {description && (
        <Text size="sm" c="dimmed" mb="sm">
          <Spoiler maxHeight={60} showLabel="Show more" hideLabel="Hide">{description}</Spoiler>
        </Text>
      )}

      {/* Extras */}
      {extras.length > 0 && (
        <Group gap="xs" mb="md">
          {extras.map((value, index) => (
            <Badge key={index} variant="outline" color="gray" radius="sm">
              {value}
            </Badge>
          ))}
        </Group>
      )}

      {/* CTA */}
      <Button component={Link} to={href} variant="light" fullWidth leftSection={<IconEye size={14} />} mt="auto">
        View details
      </Button>
    </Card>
  );
}
