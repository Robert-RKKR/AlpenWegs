import { apiClient } from "../../../services/api/client";
import type { AuthUser } from "../../../stores/authStore";

/* =========================
   Types
========================= */

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

/* =========================
   Auth API
========================= */

export async function login(
  payload: LoginPayload
): Promise<LoginResponse> {
  const response = await apiClient.post("/api/auth/login/", payload);
  return response.data.page_results;
}

export async function logout(
  refresh: string
): Promise<void> {
  await apiClient.post("/api/auth/logout/", { refresh });
}
