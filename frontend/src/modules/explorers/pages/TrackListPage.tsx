// Import application components:
import { ObjectListComponent } from "../../../components/objects/listComponent/ListComponent";
import type { TrackRelationModel } from "../models/trackModel";

// Configuration for ObjectListComponent to display TrackRelationModel:
export const objectListConfig = {
  // Base API call data:
  api: {
    listUrl: "/api/explorers/track/",
  },
  // Base page header configuration:
  header: {
    title: "Tracks",
  },
  // Card mapping configuration:
  card: {
    href: ["pk", "/explorer/track/"],
    image: ["primary_photo"],
    title: ["name"],
    description: ["snippet"],
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
