// Application import:
import type { ApiListResponse, ApiDetailResponse } from "./types";

// Axios import:
import type { AxiosResponse } from "axios";

// Helper functions to unwrap API responses:
export function unwrapList<T>(
  response: AxiosResponse<ApiListResponse<T>>
): ApiListResponse<T> {
  return response.data;
}

// Helper function to unwrap detail response:
export function unwrapDetail<T>(
  response: AxiosResponse<ApiDetailResponse<T>>
): T {
  return response.data.page_results;
}
