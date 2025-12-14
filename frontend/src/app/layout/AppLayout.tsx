import { Outlet } from "react-router-dom";
import { PageFooter } from "../../components/layout/PageFooter";
import { PageHeader } from "../../components/layout/PageHeader";

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
