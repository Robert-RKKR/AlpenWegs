import { apiClient } from "./client";
import { unwrapList, unwrapDetail } from "./helpers";
import type { ApiListResponse, ApiDetailResponse } from "./types";

export class BaseApi {
  static list<T>(
    url: string,
    params?: Record<string, unknown>
  ): Promise<ApiListResponse<T>> {
    return apiClient
      .get<ApiListResponse<T>>(url, { params })
      .then(unwrapList);
  }

  static detail<T>(
    url: string
  ): Promise<T> {
    return apiClient
      .get<ApiDetailResponse<T>>(url)
      .then(unwrapDetail);
  }
}
