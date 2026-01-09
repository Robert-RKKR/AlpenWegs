// Application imports:
import { StateLoader } from "../../elements/stateLoader/StateLoader";
import type { ApiListResponse } from "../../../services/api/types";
import { Pagination } from "../../../services/ui/Pagination";
import { BaseApi } from "../../../services/api/baseApi";
import { ObjectCard } from "../cards/ObjectCard";

// Mantine imports:
import { Grid, Stack, Title, Center } from "@mantine/core";

// React imports:
import { useQuery } from "@tanstack/react-query";
import { useState } from "react";

// Import component css:
import "./ListComponent.css";

// Helpers:
function resolvePath(obj: any, path?: string[]) {
  if (!path) return undefined;
  return path.reduce((acc, key) => acc?.[key], obj);
}

// Types (unchanged)
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
      ? resolvePath(data.page_results[0], config.header.title.value)
      : config.header?.title?.fallback;

  return (
    <Stack gap="lg">
      {/* Header */}
      {resolvedHeaderTitle && (
        <Title order={2}>{resolvedHeaderTitle}</Title>
      )}

      {/* Loading */}
      {isLoading && (
        <Center py="xl">
          <StateLoader />
        </Center>
      )}

      {/* Error */}
      {!isLoading && error && (
        <Center py="xl">
          <Title order={4} c="red">
            Failed to load data
          </Title>
        </Center>
      )}

      {/* Empty */}
      {!isLoading && !error && data && data.page_results.length === 0 && (
        <Center py="xl">
          {emptyMessage}
        </Center>
      )}

      {/* Data grid */}
      {!isLoading && !error && data && data.page_results.length > 0 && (
        <Grid gutter="md">
          {data.page_results.map((item: any) => {
            const href =
              config.card.href.base +
              (item[config.card.href.id] ?? "");

            return (
              <Grid.Col
                key={item.pk ?? crypto.randomUUID()}
                span={{ base: 12, sm: 6, md: 4, lg: 3, xl: 2 }}
              >
                <ObjectCard
                  href={href}
                  image={
                    resolvePath(item, config.card.image?.value) ??
                    undefined
                  }
                  title={
                    resolvePath(item, config.card.title?.value) ?? ""
                  }
                  description={
                    resolvePath(item, config.card.description?.value) ??
                    ""
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
              </Grid.Col>
            );
          })}
        </Grid>
      )}

      {/* Footer / Pagination */}
      {!isLoading && !error && data && data.page_results.length > 0 && (
        <Center pt="md">
          <Pagination
            page={page}
            pageCount={data.page_count}
            onChange={setPage}
          />
        </Center>
      )}
    </Stack>
  );
}
