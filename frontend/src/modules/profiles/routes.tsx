import { Routes, Route } from "react-router-dom";
import { LoginPage } from "./pages/auth/LoginPage";
import { UserPage } from "./pages/user/UserPage";
import { CardsPage } from "./pages/user/UserCardsPage";
import { DashboardPage } from "./pages/user/UserDashboardPage";

export function AuthRoutes() {
  return (
    <Routes>
      <Route path="login" element={<LoginPage />} />
      <Route path="profile" element={<UserPage />} />
      <Route path="cards" element={<CardsPage />} />
      <Route path="dashboard" element={<DashboardPage />} />
    </Routes>
  );
}
