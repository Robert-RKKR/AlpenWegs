// Import React components:
import { QueryClientProvider } from "@tanstack/react-query";
import { queryClient } from "./providers/queryClient";
import { BrowserRouter } from "react-router-dom";

// Import application components:
import { AppRoutes } from "./routes";

export function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </QueryClientProvider>
  );
}
