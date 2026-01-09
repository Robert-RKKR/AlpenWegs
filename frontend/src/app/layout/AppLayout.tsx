// Imports:
import { PageFooter } from "./pageFooter/PageFooter";
import { PageHeader } from "./pageHeader/PageHeader";
import { Outlet } from "react-router-dom";
import { AppShell } from "@mantine/core";

// Main Component Function:
export function AppLayout() {
  return (
    <AppShell
      header={{ height: 60 }}
      footer={{ height: "auto" }}
      padding="md"
    >
      {/* Top bar */}
      <AppShell.Header>
        <PageHeader />
      </AppShell.Header>

      {/* Main routed content */}
      <AppShell.Main>
        <Outlet />
      </AppShell.Main>

      {/* Footer */}
      <AppShell.Footer>
        <PageFooter />
      </AppShell.Footer>
    </AppShell>
  );
}
