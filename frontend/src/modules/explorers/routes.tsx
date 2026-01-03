//  Application imports:
import { TrackRetrievePage } from "./pages/TrackRetrievePage";
import { TrackEditPage } from "./pages/TrackEditPage";
import { TrackListPage } from "./pages/TrackListPage";

// React imports:
import { Routes, Route } from "react-router-dom";

// ExplorerRoutes component:
export function ExplorerRoutes() {
  return (
    <Routes>
      <Route path="track/:id/edit" element={<TrackEditPage />} />
      <Route path="track/:id" element={<TrackRetrievePage />} />
      <Route path="track" element={<TrackListPage />} />
    </Routes>
  );
}
