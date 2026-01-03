// Application imports:
import { StateLoader } from "../../elements/stateLoader/StateLoader";
import { Pagination } from "../../../services/ui/Pagination";
import { ObjectCard } from "../cards/ObjectCard";
import type { ApiListResponse } from "../../../services/api/types";
import { BaseApi } from "../../../services/api/baseApi";

// React imports:
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";

// Import component css:
import "./ListComponent.css";

// Helpers functions:
function resolvePath(obj: any, path?: string[]) {
  if (!path) return undefined;
  return path.reduce((acc, key) => acc?.[key], obj);
}

// Properties:
type ObjectListProps<TModel> = {
  config: {
    api: {
      listUrl: string;
    };
    header?: {
      title?: string;
    };
    card: any;
  };
  emptyMessage?: string;
};

// ObjectListComponent component:
export function ObjectListComponent<TModel>({
  config,
  emptyMessage = "No items found",
}: ObjectListProps<TModel>) {
  const [page, setPage] = useState(1);

  const { data, isLoading, error } = useQuery<ApiListResponse<TModel>>({
    queryKey: [config.api.listUrl, page],
    queryFn: () =>
      BaseApi.list<TModel>(config.api.listUrl, {
        page_number: page,
      }),
    placeholderData: (prev) => prev,
  });

  return (
    <>
      {/* Header */}
      {config.header?.title && (
        <div className="objects-header card-box">
          <h2>{config.header.title}</h2>
        </div>
      )}

      {/* Body */}
      {isLoading && (
        <div className="objects-body-loading">
          <StateLoader />
        </div>
      )}

      {!isLoading && error && (
        <div className="objects-body objects-empty">
          <p>Failed to load data</p>
        </div>
      )}

      {!isLoading && !error && data && data.page_results.length === 0 && (
        <div className="objects-body objects-empty">
          {emptyMessage}
        </div>
      )}

      {!isLoading && !error && data && data.page_results.length > 0 && (
        <div className="objects-body">
          {data.page_results.map((item: any) => (
            <ObjectCard
              key={item.pk ?? crypto.randomUUID()}
              href={
                config.card.href[1] +
                item[config.card.href[0]]
              }
              image={resolvePath(item, config.card.image)}
              title={resolvePath(item, config.card.title)}
              description={
                resolvePath(item, config.card.description) ?? ""
              }
              properties={
                config.card.properties?.map(
                  (p: any) =>
                    `${resolvePath(item, p.value) ?? ""}${p.suffix ?? ""}`,
                ) ?? []
              }
              extras={
                config.card.extras?.map(
                  (e: any) =>
                    `${resolvePath(item, e.value) ?? ""}${e.suffix ?? ""}`,
                ) ?? []
              }
            />
          ))}
        </div>
      )}

      {/* Footer */}
      {!isLoading &&
        !error &&
        data &&
        data.page_results.length > 0 && (
          <div className="objects-footer">
            <Pagination
              page={page}
              pageCount={data.page_count}
              onChange={setPage}
            />
          </div>
        )}
    </>
  );
}
