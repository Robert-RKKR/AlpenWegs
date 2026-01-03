// Import application components:
import { ObjectContainer } from "../../../components/objects/container/ObjectContainer";
import type { TrackRelationModel } from "../models/trackModel";
import { TrackApi } from "../api/trackApi";

// ExplorerTracksPage component:
export function ExplorerTracksPage() {
  return (
    <div className="objects">
      <div className="objects-header card-box">
        <h2>Tracks</h2>
      </div>

      <ObjectContainer<TrackRelationModel>
        queryKey={(page) => ["track", "relation", page]}
        queryFn={(page) =>
          TrackApi.light({ page_number: page })
        }
        renderCard={(track) => ({
          href: `/explorer/track/${track.pk}`,
          image: track.primary_photo,
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
