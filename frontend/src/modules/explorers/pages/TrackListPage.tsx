// Import application components:
import { ObjectListComponent } from "../../../components/objects/list/ListComponent";
import type { TrackRelationModel } from "../models/trackModel";

// Configuration for ObjectListComponent to display TrackRelationModel:
export const objectListConfig = {
  // Base API call data:
  api: {
    listUrl: "/api/explorers/track/",
  },
  // Base page header configuration:
  header: {
    title: {
      key: "page_title",
      label: "Title",
      value: ["name"],
      fallback: "Tracks",
    },
  },
  // Card mapping configuration:
  card: {
    href: {
      base: "/explorer/track/",
      id: "pk",
    },
    image: {
      key: "primary_photo",
      label: "Primary Photo",
      value: ["primary_photo"],
    },
    title: {
      key: "name",
      label: "Name",
      value: ["name"],
    },
    description: {
      key: "snippet",
      label: "Description",
      value: ["snippet"],
    },
    properties: [
      { key: "category", value: ["category", "label"] },
      {
        key: "difficulty",
        value: ["category_specific_difficulty", "label"],
      },
      {
        key: "distance",
        value: ["total_distance"],
        suffix: " m",
      },
      {
        key: "elevation",
        value: ["elevation_gain"],
        suffix: " m",
      },
    ],
    extras: [
      {
        key: "avg_speed",
        value: ["average_speed"],
        suffix: " km/h",
      },
      {
        key: "max_speed",
        value: ["maximum_speed"],
        suffix: " km/h",
      },
      {
        key: "time",
        value: ["moving_time"],
        suffix: " min",
      },
    ],
  },
};

// TrackListPage component:
export function TrackListPage() {
  return (
    <ObjectListComponent<TrackRelationModel>
      config={objectListConfig}
      emptyMessage="No tracks available."
    />
  );
}
