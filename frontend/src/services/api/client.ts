// Application import:
import { useAuthStore } from "../../stores/authStore";

// Axios import:
import axios from "axios";

// API client configuration:
export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor to add auth token:
apiClient.interceptors.request.use((config) => {

  // Get auth state from Zustand store:
  const { accessToken, isAuthenticated } = useAuthStore.getState();

  // If authenticated, add the access token to headers:
  if (isAuthenticated && accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  // Return the modified config:
  return config;
});
