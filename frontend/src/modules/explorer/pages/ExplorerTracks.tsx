import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

import { TrackApi } from "../api/trackApi";
import type { TrackRelationModel } from "../models/trackModel";
import type { ApiListResponse } from "../../../services/api/types";
import { Pagination } from "../../../services/ui/Pagination";

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
    <div>
      <ul>
        {data.page_results.map((track) => (
          <li key={track.pk}>{track.name}</li>
        ))}
      </ul>

      <Pagination
        page={page}
        pageCount={data.page_count}
        onChange={setPage}
      />
    </div>
  );
}
