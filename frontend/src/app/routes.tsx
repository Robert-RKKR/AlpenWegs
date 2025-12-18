// Import application components:
import { ExplorerRoutes } from "../modules/explorers/routes";
import { NotFoundPage } from "./pages/NotFoundPage";
import { AppLayout } from "./layout/AppLayout";
import { AuthRoutes } from "../modules/profiles/routes";

// Import React components:
import { Routes, Route } from "react-router-dom";

// Main Component Function:
export function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        {/* Home Page */}
        <Route path="/" element={<div>Home</div>} />

        {/* Explorers Pages */}
        <Route path="/explorer/*" element={<ExplorerRoutes />} />

        {/* Auth Pages */}
        <Route path="/auth/*" element={<AuthRoutes />} />
        
        {/* 404 Page Not Found */}
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  );
}
