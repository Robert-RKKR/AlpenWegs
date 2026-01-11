// Imports:
import { Grid, Stack, Title, Center, Loader, Accordion, TextInput, RangeSlider } from "@mantine/core";
import { ErrorWindow } from "../../elements/errorWindow/ErrorWindow";
import type { ApiListResponse } from "../../../services/api/types";
import { IconDatabaseOff, IconInbox } from "@tabler/icons-react";
import { Pagination } from "../../elements/pagination/Pagination";
import { BaseApi } from "../../../services/api/baseApi";
import { PageContent } from "../../content/PageContent";
import { useQuery } from "@tanstack/react-query";
import { ObjectCard } from "./card/ObjectCard";
import { useState } from "react";

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
      title?: string;
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

  const searchData = [
    {
      emoji: '🍎',
      value: 'Apples',
      description:
        'Crisp and refreshing fruit. Apples are known for their versatility and nutritional benefits. They come in a variety of flavors and are great for snacking, baking, or adding to salads.',
    },
    {
      emoji: '🍌',
      value: 'Bananas',
      description:
        'Naturally sweet and potassium-rich fruit. Bananas are a popular choice for their energy-boosting properties and can be enjoyed as a quick snack, added to smoothies, or used in baking.',
    },
    {
      emoji: '🥦',
      value: 'Broccoli',
      description:
        'Nutrient-packed green vegetable. Broccoli is packed with vitamins, minerals, and fiber. It has a distinct flavor and can be enjoyed steamed, roasted, or added to stir-fries.',
    },
  ];

  const searchItems = searchData.map((item) => (
    <Accordion.Item key={item.value} value={item.value}>
      <Accordion.Control icon={item.emoji}>{item.value}</Accordion.Control>
      <Accordion.Panel>{item.description}</Accordion.Panel>
    </Accordion.Item>
  ));

  const listTitle = config.header?.title;

  return (
    <Stack gap="lg">

      {/* Loading */}
      {isLoading && (
        <Center py="xl">
          <Loader />
        </Center>
      )}

      {/* Error */}
      {!isLoading && error && (
        <ErrorWindow icon={IconDatabaseOff} title="Failed to load data" description="The server returned an error while loading this list."/>
      )}

      {/* Empty */}
      {!isLoading && !error && data && data.page_results.length === 0 && (
        <ErrorWindow icon={IconInbox} title="Nothing here yet" description={emptyMessage}/>
      )}

      {/* Data grid */}
      {!isLoading && !error && data && data.page_results.length > 0 && (
        <PageContent type="menu">
          {/* LEFT MENU */}
          <PageContent.Item area="menu">
            <Accordion defaultValue="Apples">
              {/* { searchItems } */}
              <Accordion.Item key="nameSearch" value="Name Search">
                <Accordion.Control icon="🍎">Name Search</Accordion.Control>
                <Accordion.Panel>
                  <TextInput label="Name" placeholder="Name..." error="Invalid name"/>
                </Accordion.Panel>
              </Accordion.Item>
              <Accordion.Item key="distanceSearch" value="Distance Search">
                <Accordion.Control icon="📏">Distance Search</Accordion.Control>
                <Accordion.Panel>
                  <RangeSlider mb="md" color="blue" max={100} defaultValue={[10, 30]} marks={[
                    { value: 20, label: '20 Km' },
                    { value: 40, label: '40 Km' },
                    { value: 60, label: '60 Km' },
                    { value: 80, label: '80 Km' },
                  ]} />
                  <TextInput label="Name" placeholder="Name..." error="Invalid name"/>
                </Accordion.Panel>
              </Accordion.Item>
            </Accordion>
          </PageContent.Item>


          {/* RIGHT CONTENT */}
          <PageContent.Item area="content">
            {/* Header */}
            <Title order={2}>{listTitle}</Title>

            {/* Cards */}
            <Grid gutter="md">
              {data.page_results.map((item: any) => {
                const href =
                  config.card.href.base +
                  (item[config.card.href.id] ?? "");

                return (
                  <Grid.Col key={item.pk ?? crypto.randomUUID()} span={{ base: 12, sm: 6, md: 4, lg: 3, xl: 3 }}>
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
            <Center pt="md">
              <Pagination page={page} pageCount={data.page_count} onChange={setPage}/>
            </Center>
          </PageContent.Item>
        </PageContent>
      )}
    </Stack>
  );
}
