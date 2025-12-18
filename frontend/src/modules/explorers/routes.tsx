import { Routes, Route } from "react-router-dom";
import { ExplorerTracks } from "./pages/Tracks";
import { RouteDetailPage } from "./pages/RouteDetailPage";

export function ExplorerRoutes() {
  return (
    <Routes>
      <Route path="tracks" element={<ExplorerTracks />} />
      <Route path="routes/:id" element={<RouteDetailPage />} />
    </Routes>
  );
}