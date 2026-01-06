// Application import:
import { apiClient } from "../../../services/api/client";
import type { AuthUser } from "../../../stores/authStore";

// Axios import:
import axios from "axios";

// Type definitions:
export type LoginPayload = {
  email: string;
  password: string;
};

export type LoginResponse = {
  access: string;
  refresh: string;
  user: AuthUser;
};

export type LogoutPayload = {
  refresh: string;
};

// Login function:
export async function login(
  payload: LoginPayload
): Promise<LoginResponse> {
  const response = await apiClient.post("/api/auth/login/", payload);
  return response.data.page_results;
}

// Logout function:
export async function logout(
  refresh: string
): Promise<void> {
  await apiClient.post("/api/auth/logout/", { refresh });
}

// Refresh token function:
export async function refreshToken(refresh: string): Promise<string> {
  const response = await axios.post(
    `${import.meta.env.VITE_API_BASE_URL}/api/auth/token/refresh/`,
    { refresh },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );

  return response.data.access;
}
