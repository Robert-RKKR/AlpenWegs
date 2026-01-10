// Imports:
import { PageHeader } from "./pageHeader/PageHeader";
import { PageFooter } from "./pageFooter/PageFooter";
import { PageBody } from "./pageBody/PageBody";
import { AppShell } from "@mantine/core";

// Main Component Function:
export function AppLayout() {
  return (
    <AppShell header={{ height: 60 }} footer={{ height: "auto" }} padding={0}>
      {/* Header */}
      <AppShell.Header>
        <PageHeader />
      </AppShell.Header>

      {/* Main body (scrollable, centered) */}
      <AppShell.Main>
        <PageBody />
      </AppShell.Main>

      {/* Footer (permanent) */}
      <AppShell.Footer>
        <PageFooter />
      </AppShell.Footer>
    </AppShell>
  );
}
