import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

import { TrackApi } from "../api/trackApi";
import type { TrackRelationModel } from "../models/trackModel";
import type { ApiListResponse } from "../../../services/api/types";
import { Pagination } from "../../../services/ui/Pagination";

// Import component css:
import "./BoxContainer.css";

export function ExplorerTracks() {
  const [page, setPage] = useState(1);

  const { data, isLoading, error } = useQuery<
    ApiListResponse<TrackRelationModel>
  >({
    queryKey: ["tracks", "relation", page],
    queryFn: () =>
      TrackApi.light({ page_number: page }),
    placeholderData: (previousData) => previousData,
  });

  if (isLoading) return <div>Loading tracks…</div>;
  if (error || !data) return <div>Failed to load tracks</div>;

  return (
    <div className="box-container-objects">
      <div className="box-container-heder">
        <h2>Tracks</h2>
      </div>
      
      <div className="box-container-body">
        <ul>
          {data.page_results.map((track) => (
            <li key={track.pk}>{track.name} {track.total_distance ?? 0} m</li>
          ))}
        </ul>
      </div>

      <div className="box-container-footer">
        <Pagination
          page={page}
          pageCount={data.page_count}
          onChange={setPage}
        />
      </div>
    </div>
  );
}
