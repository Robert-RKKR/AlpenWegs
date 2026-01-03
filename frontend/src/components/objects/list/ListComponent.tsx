// Application imports:
import { StateLoader } from "../../elements/stateLoader/StateLoader";
import type { ApiListResponse } from "../../../services/api/types";
import { Pagination } from "../../../services/ui/Pagination";
import { BaseApi } from "../../../services/api/baseApi";
import { ObjectCard } from "../cards/ObjectCard";

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
type ResolvedFieldConfig = {
  key: string;
  label?: string;
  value?: string[];
  suffix?: string;
  fallback?: string;
};
type HrefFieldConfig = {
  id: string;
  base: string;
  value?: string[];
};
type ObjectListProps<TModel> = {
  config: {
    api: {
      listUrl: string;
    };

    header?: {
      title?: ResolvedFieldConfig;
    };

    card: {
      href: HrefFieldConfig;
      image?: ResolvedFieldConfig;
      title?: ResolvedFieldConfig;
      description?: ResolvedFieldConfig;

      properties?: ResolvedFieldConfig[];
      extras?: ResolvedFieldConfig[];
    };
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

  const resolvedHeaderTitle =
    config.header?.title?.value && data?.page_results?.[0]
      ? resolvePath(
          data.page_results[0],
          config.header.title.value,
        )
      : config.header?.title?.fallback;

  return (
    <>
      {/* Header */}
      {resolvedHeaderTitle && (
        <div className="objects-header card-box">
          <h2>{resolvedHeaderTitle}</h2>
        </div>
      )}

      {/* Loading */}
      {isLoading && (
        <div className="objects-body-loading">
          <StateLoader />
        </div>
      )}

      {/* Error */}
      {!isLoading && error && (
        <div className="objects-body objects-empty">
          <p>Failed to load data</p>
        </div>
      )}

      {/* Empty */}
      {!isLoading && !error && data && data.page_results.length === 0 && (
        <div className="objects-body objects-empty">
          {emptyMessage}
        </div>
      )}

      {/* Data */}
      {!isLoading && !error && data && data.page_results.length > 0 && (
        <div className="objects-body">
          {data.page_results.map((item: any) => {
            const hrefBase =
              resolvePath(item, config.card.href.value) ??
              "";

            const href =
              config.card.href.base +
              (item[config.card.href.id] ?? "");

            return (
              <ObjectCard
                key={item.pk ?? crypto.randomUUID()}
                href={href}
                image={
                  resolvePath(
                    item,
                    config.card.image?.value,
                  ) ?? undefined
                }
                title={
                  resolvePath(
                    item,
                    config.card.title?.value,
                  ) ?? ""
                }
                description={
                  resolvePath(
                    item,
                    config.card.description?.value,
                  ) ?? ""
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
            );
          })}
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
