//  Imports:
import { Button, Container, Image, SimpleGrid, Text, Title } from '@mantine/core';
import { Link } from "react-router-dom";
import classes from "./NotFoundPage.module.css";
import image from './404.svg';

// Main Page Function:
export function NotFoundPage() {
  return (
    <Container className={classes.root}>
      <SimpleGrid spacing={{ base: 40, sm: 80 }} cols={{ base: 1, sm: 2 }}>
        <Image src={image} className={classes.mobileImage} />
        <div>
          <Title className={classes.title}>Something is not right...</Title>
          <Text c="dimmed" size="lg">
            Page you are trying to open does not exist. You may have mistyped the address, or the
            page has been moved to another URL. If you think this is an error contact support.
          </Text>
          <Button variant="outline" size="md" mt="xl" className={classes.control} component={Link} to="/">
            Get back to home page
          </Button>
        </div>
      </SimpleGrid>
    </Container>
  );
}
