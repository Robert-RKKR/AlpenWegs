//  Application imports:
import { TrackRetrievePage } from "./pages/TrackRetrievePage";
import { TrackListPage } from "./pages/TrackListPage";

// React imports:
import { Routes, Route } from "react-router-dom";

// ExplorerRoutes component:
export function ExplorerRoutes() {
  return (
    <Routes>
      <Route path="track" element={<TrackListPage />} />
      <Route path="track/:id" element={<TrackRetrievePage />} />
    </Routes>
  );
}
