import { Routes, Route } from "react-router-dom";
import { LoginPage } from "./pages/LoginPage";
import { ProfilePage } from "./pages/ProfilePage";
import { CardsPage } from "./pages/CardsPage";
import { DashboardPage } from "./pages/DashboardPage";

export function AuthRoutes() {
  return (
    <Routes>
      <Route path="login" element={<LoginPage />} />
      <Route path="profile" element={<ProfilePage />} />
      <Route path="cards" element={<CardsPage />} />
      <Route path="dashboard" element={<DashboardPage />} />
    </Routes>
  );
}
