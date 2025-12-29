import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

import { ObjectCard } from "../cards/ObjectCard";
import { Pagination } from "../../../services/ui/Pagination";
import type { ApiListResponse } from "../../../services/api/types";
import type { ObjectCardProps } from "../types";
import "./ObjectContainer.css";

type ObjectContainerProps<TModel> = {
  queryKey: (page: number) => readonly unknown[];
  queryFn: (page: number) => Promise<ApiListResponse<TModel>>;
  renderCard: (item: TModel) => ObjectCardProps;
  emptyMessage?: string;
};

export function ObjectContainer<TModel>({
  queryKey,
  queryFn,
  renderCard,
  emptyMessage = "No items found",
}: ObjectContainerProps<TModel>) {
  const [page, setPage] = useState(1);

  const { data, isLoading, error } = useQuery<ApiListResponse<TModel>>({
    queryKey: queryKey(page),
    queryFn: () => queryFn(page),
    placeholderData: (prev) => prev,
  });

  if (isLoading) {
    return <div className="objects-body">Loading…</div>;
  }

  if (error || !data) {
    return <div className="objects-body">Failed to load data</div>;
  }

  if (!data.page_results.length) {
    return (
      <div className="objects-body objects-empty">
        {emptyMessage}
      </div>
    );
  }

  return (
    <>
      <div className="objects-body">
        {data.page_results.map((item) => (
          <ObjectCard
            key={(item as any).pk ?? crypto.randomUUID()}
            {...renderCard(item)}
          />
        ))}
      </div>

      <div className="objects-footer">
        <Pagination
          page={page}
          pageCount={data.page_count}
          onChange={setPage}
        />
      </div>
    </>
  );
}
