// src/services/auth/authApi.ts
import { apiClient } from "../../../services/api/client";
import type { AuthUser } from "../../../stores/authStore";

export type LoginPayload = {
  email: string;
  password: string;
};

export type LoginResponse = {
  access: string;
  refresh: string;
  user: AuthUser;
};

export async function login(
  payload: LoginPayload
): Promise<LoginResponse> {
  const response = await apiClient.post("/api/auth/login/", payload);
  return response.data.page_results;
}
