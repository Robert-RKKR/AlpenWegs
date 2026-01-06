//  Application import:
import { useAuthStore } from "../../../stores/authStore";
import { refreshToken } from "./authApi";

let refreshInterval: number | null = null;

export function startTokenRefresh() {
  stopTokenRefresh();

  refreshInterval = window.setInterval(async () => {
    const {
      refreshToken: refresh,
      rememberMe,
      isAuthenticated,
      updateAccessToken,
      clearAuth,
    } = useAuthStore.getState();

    if (!rememberMe || !isAuthenticated || !refresh) return;

    try {
      const newAccess = await refreshToken(refresh);
      updateAccessToken(newAccess);
    } catch {
      clearAuth();
      stopTokenRefresh();
    }
  }, 5 * 60 * 1000);
}

export function stopTokenRefresh() {
  if (refreshInterval) {
    clearInterval(refreshInterval);
    refreshInterval = null;
  }
}
