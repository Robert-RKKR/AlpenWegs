// Application imports:
import type { ApiListResponse, ApiDetailResponse } from "./types";
import { unwrapList, unwrapDetail } from "./helpers";
import { apiClient } from "./client";

// BaseApi class:
export class BaseApi {
  static list<T>(
    url: string,
    params?: Record<string, unknown>
  ): Promise<ApiListResponse<T>> {
    return apiClient
      .get<ApiListResponse<T>>(url, { params })
      .then(unwrapList);
  }

  static retrieve<T>(
    url: string
  ): Promise<T> {
    return apiClient
      .get<ApiDetailResponse<T>>(url)
      .then(unwrapDetail);
  }
  
  static update<T>(
    url: string,
    data: Partial<T>
  ): Promise<T> {
    return apiClient
      .patch<ApiDetailResponse<T>>(url, data)
      .then(unwrapDetail);
  }
}
