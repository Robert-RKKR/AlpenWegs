// Imports:
import classes from "./PageBody.module.css";
import { Outlet } from "react-router-dom";
import { Box, Center } from "@mantine/core";

// PageBody component:
export function PageBody() {
  return (
    <Box className={classes.body}>
      <Outlet />
    </Box>
  );
}
