// Application imports:
import { ObjectRetrieveComponent } from "../../../components/objects/retrieve/RetrieveComponent";
import type { TrackDetailedModel } from "../models/trackModel";

// Configuration for ObjectRetrieveComponent to display TrackRelationModel:
export const trackRetrieveConfig = {
  // Base API call data:
  api: {
    listUrl: "/api/explorers/track/",
  },
  // Base page header configuration:
  header: {
    title: "Tracks",
  },
  // Object mapping configuration:
  image: ["primary_photo"],
  properties: [
    {
      key: "distance",
      label: "Distance",
      value: ["total_distance"],
      suffix: " m",
    },
    {
      key: "elevation_gain",
      label: "Elevation gain",
      value: ["elevation_gain"],
      suffix: " m",
    },
  ],
  chapters: [
    {
      title: "Statistics",
      properties: [
        {
          key: "avg_speed",
          label: "Avg speed",
          value: ["average_speed"],
          suffix: " km/h",
        },
        {
          key: "max_speed",
          label: "Max speed",
          value: ["maximum_speed"],
          suffix: " km/h",
        },
      ],
    },
    {
      title: "Other information",
      properties: [
        {
          key: "elevation",
          label: "Elevation",
          value: ["elevation_gain"],
          suffix: " m",
        },
      ],
    },
  ],
};

// TracksRetrievePage component:
export function TrackRetrievePage() {
  return (
    <ObjectRetrieveComponent<TrackDetailedModel>
      config={trackRetrieveConfig}
    />
  );
}
