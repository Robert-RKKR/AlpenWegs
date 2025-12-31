// Application imports:
import { ObjectDetails } from "../../../components/objects/details/ObjectDetails";
import type { TrackDetailedModel } from "../models/trackModel";
import { TrackApi } from "../api/trackApi";

// ExplorerTrackDetailsPage component:
export function ExplorerTrackDetailsPage() {
  return (
    <ObjectDetails<TrackDetailedModel>
      queryKey={(id) => ["track", "details", id]}
      queryFn={(id) => TrackApi.retrieve(id)}
      mapDetails={(track) => ({
        image: track.primary_photo,
        title: track.name,

        properties: [
          { label: "Distance", value: `${track.total_distance} m` },
          { label: "Elevation gain", value: `${track.elevation_gain} m` },
        ],

        chapters: [
          {
            title: "Statistics",
            properties: [
              { label: "Avg speed", value: `${track.average_speed} km/h` },
              { label: "Max speed", value: `${track.maximum_speed} km/h` },
            ],
          },
        ],
      })}
    />
  );
}
