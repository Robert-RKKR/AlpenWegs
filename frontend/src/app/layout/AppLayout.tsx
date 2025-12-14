// Import application components:
import { PageFooter } from "../../components/layout/PageFooter";
import { PageHeader } from "../../components/layout/PageHeader";

// Import React components:
import { Outlet } from "react-router-dom";

// Main Component Function:
export function AppLayout() {
  return (
    <div className="main-page">
      {/* Main Page Header */}
      <PageHeader />

      {/* Main Page Content */}
      <main className="page-body">
        <Outlet />
      </main>

      {/* Main Page Footer */}
      <PageFooter />
    </div>
  );
}
