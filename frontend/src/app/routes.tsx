import { Routes, Route } from "react-router-dom";
import { AppLayout } from "./layout/AppLayout";
import { ExplorerRoutes } from "../modules/explorer/routes";
import { NotFoundPage } from "./pages/NotFoundPage";

export function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route path="/" element={<div>Home</div>} />
        <Route path="/explorer/*" element={<ExplorerRoutes />} />
        
        {/* 404 Page Not Found */}
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  );
}
