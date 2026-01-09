// Import application components:
// import { PageFooter } from "../../components/layout/PageFooter";
import { PageHeader } from "../../components/layout/PageHeader";

// Import React components:
import { Outlet } from "react-router-dom";
import { AppShell } from "@mantine/core";

// Main Component Function:
export function AppLayout() {
  return (
    <AppShell
      header={{ height: 60 }}
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
    </AppShell>
  );
}
