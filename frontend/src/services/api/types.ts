export type PageLinks = {
  page_next: string | null;
  page_previous: string | null;
};

export type ApiBaseResponse = {
  page_status: boolean;
  page_error: string | null;
};

export type ApiListResponse<T> = ApiBaseResponse & {
  page_results: T[];
  page_objects: number;
  page_count: number;
  page_links: PageLinks;
};

export type ApiDetailResponse<T> = ApiBaseResponse & {
  page_results: T;
};
