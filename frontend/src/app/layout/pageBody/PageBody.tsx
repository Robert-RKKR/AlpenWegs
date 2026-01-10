// Imports:
import { ScrollArea } from "@mantine/core";
import { Outlet } from "react-router-dom";
import classes from "./PageBody.module.css";

// PageBody component:
export function PageBody() {
  return (
    <ScrollArea className={classes.scroll} type="auto" scrollbarSize={8}>
      <main className={classes.body}>
        <Outlet />
      </main>
    </ScrollArea>
  );
}
