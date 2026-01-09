//  Application imports:
import { HomePage } from "./pages/HomePage";

// React imports:
import { Routes, Route } from "react-router-dom";

// HomeRoutes component:
export function HomeRoutes() {
  return (
    <Routes>
      <Route path="" element={<HomePage />} />
    </Routes>
  );
}
