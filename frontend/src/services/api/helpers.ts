import type { AxiosResponse } from "axios";
import type { ApiListResponse, ApiDetailResponse } from "./types";

export function unwrapList<T>(
  response: AxiosResponse<ApiListResponse<T>>
): ApiListResponse<T> {
  return response.data;
}

export function unwrapDetail<T>(
  response: AxiosResponse<ApiDetailResponse<T>>
): T {
  return response.data.page_results;
}
