// Imports:
import { Box, Flex, ScrollArea, Divider } from "@mantine/core";
import classes from "./PageContent.module.css";
import { useMediaQuery } from "@mantine/hooks";
import type { ReactNode } from "react";

type PageContentType = "full" | "menu";
type PageContentArea = "menu" | "content";

type PageContentProps = {
  type: PageContentType;
  children: ReactNode;
};

type PageContentItemProps = {
  area: PageContentArea;
  children: ReactNode;
};

function PageContentItem({ children }: PageContentItemProps) {
  return <>{children}</>;
}

export function PageContent({ children }: PageContentProps) {

  // Responsive check:
  const isMobile = useMediaQuery("(max-width: 48em)");

  // Menu layout
  const items = Array.isArray(children) ? children : [children];

  const menu = items.find(
    (child: any) => child?.props?.area === "menu",
  );
  const content = items.find(
    (child: any) => child?.props?.area === "content",
  );

  if (isMobile) {
    return (
      <ScrollArea h="100%">
        <Box p="md">
          {/* Menu first */}
          <Box mb="md">{menu}</Box>

          <Divider my="sm" />

          {/* Content full width */}
          <Box>{content}</Box>
        </Box>
      </ScrollArea>
    );
  }

  return (
    <Flex h="100%" align="stretch">
      
      {/* Left Content */}
      <Box w={280} className={classes.leftContent}>
        <ScrollArea>
          <Box>{menu}</Box>
        </ScrollArea>
      </Box>

      <Divider orientation="vertical" size="xs" />

      {/* RIGHT CONTENT */}
      <Box flex={1}>
        <ScrollArea className={classes.rightContentScrollArea} offsetScrollbars scrollbarSize={6} scrollHideDelay={100}>
          <Box p="md">{content}</Box>
        </ScrollArea>
      </Box>

    </Flex>
  );
}

PageContent.Item = PageContentItem;
