// src/stores/authStore.ts
import { create } from "zustand";

export type AuthUser = {
  pk: string;
  email: string;
  first_name: string;
  last_name: string;
};

type AuthState = {
  isAuthenticated: boolean;
  user: AuthUser | null;
  accessToken: string | null;
  refreshToken: string | null;

  setAuth: (
    user: AuthUser,
    access: string,
    refresh: string
  ) => void;

  clearAuth: () => void;
};

export const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: false,
  user: null,
  accessToken: null,
  refreshToken: null,

  setAuth: (user, access, refresh) =>
    set({
      isAuthenticated: true,
      user,
      accessToken: access,
      refreshToken: refresh,
    }),

  clearAuth: () =>
    set({
      isAuthenticated: false,
      user: null,
      accessToken: null,
      refreshToken: null,
    }),
}));
