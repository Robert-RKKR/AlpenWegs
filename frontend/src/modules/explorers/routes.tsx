//  Application imports:
import { ExplorerTrackDetailsPage } from "./pages/ExplorerTrackDetailsPage";
import { ExplorerTracksPage } from "./pages/ExplorerTracksPage";

// React imports:
import { Routes, Route } from "react-router-dom";

// ExplorerRoutes component:
export function ExplorerRoutes() {
  return (
    <Routes>
      <Route path="track" element={<ExplorerTracksPage />} />
      <Route path="track/:id" element={<ExplorerTrackDetailsPage />} />
    </Routes>
  );
}
