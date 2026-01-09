// Import application components:
import { startTokenRefresh } from "../modules/profiles/api/refreshApi";
import { useAuthStore } from "../stores/authStore";
import { AppRoutes } from "./routes";

// Import React:
import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "./providers/queryClient";
import { BrowserRouter } from "react-router-dom";
import { useEffect } from "react";

// Mantine imports:
import { MantineProvider } from "@mantine/core";

// App component:
export function App() {
  const isAuthenticated = useAuthStore((s) => s.isAuthenticated);
  const rememberMe = useAuthStore((s) => s.rememberMe);

  useEffect(() => {
    if (isAuthenticated && rememberMe) {
      startTokenRefresh();
    }
  }, [isAuthenticated, rememberMe]);

  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider
        theme={{
          primaryColor: "teal",
          defaultRadius: "md",
        }}
      >
        <BrowserRouter>
          <AppRoutes />
        </BrowserRouter>
      </MantineProvider>
    </QueryClientProvider>
  );
}
