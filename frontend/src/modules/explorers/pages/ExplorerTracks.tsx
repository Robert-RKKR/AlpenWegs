import { ObjectContainer } from "../../../components/objects/container/ObjectContainer";
import { TrackApi } from "../api/trackApi";
import type { TrackRelationModel } from "../models/trackModel";


export function ExplorerTracks() {
  return (
    <div className="objects">
      <div className="objects-header">
        <h2></h2>
      </div>

      <ObjectContainer<TrackRelationModel>
        queryKey={(page) => ["tracks", "relation", page]}
        queryFn={(page) =>
          TrackApi.light({ page_number: page })
        }
        renderCard={(track) => ({
          href: `/tracks/${track.pk}`,
          image: <></>,
          title: track.name,
          properties: [
            track.category.label,
            track.category_specific_difficulty.label,
            `${track.total_distance ?? 0} m`,
            `${track.elevation_gain ?? 0} m`,
          ],
          description: track.snippet ?? "",
          extras: [
            `${track.average_speed ?? 0} km/h`,
            `${track.maximum_speed ?? 0} km/h`,
            `${track.moving_time ?? 0} min`,
          ],
        })}
        emptyMessage="No tracks available"
      />
    </div>
  );
}
