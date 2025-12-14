import { Routes, Route } from "react-router-dom";
import { ExplorerDashboard } from "./pages/ExplorerDashboard";
import { RouteDetailPage } from "./pages/RouteDetailPage";

export function ExplorerRoutes() {
  return (
    <Routes>
      <Route index element={<ExplorerDashboard />} />
      <Route path="routes/:id" element={<RouteDetailPage />} />
    </Routes>
  );
}