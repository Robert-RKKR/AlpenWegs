import React from "react";
import { Routes, Route } from "react-router-dom";

import MainPage from "./pages/MainPage";
import HikingPage from "./pages/HikingPage";
import LoginPage from "./pages/LoginPage";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/hiking" element={<HikingPage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  );
}
