// Zustand import:
import { persist } from "zustand/middleware";
import { create } from "zustand";

// Types:
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
  rememberMe: boolean;

  setAuth: (
    user: AuthUser,
    access: string,
    refresh: string,
    rememberMe: boolean
  ) => void;

  updateAccessToken: (access: string) => void;
  clearAuth: () => void;
};

// Store:
export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      isAuthenticated: false,
      user: null,
      accessToken: null,
      refreshToken: null,
      rememberMe: false,

      setAuth: (user, access, refresh, rememberMe) =>
        set({
          isAuthenticated: true,
          user,
          accessToken: access,
          refreshToken: refresh,
          rememberMe,
        }),

      updateAccessToken: (access) =>
        set({ accessToken: access }),

      clearAuth: () =>
        set({
          isAuthenticated: false,
          user: null,
          accessToken: null,
          refreshToken: null,
          rememberMe: false,
        }),
    }),
    {
      name: "auth-storage",
    }
  )
);
