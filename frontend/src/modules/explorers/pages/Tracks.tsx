import { useState } from "react";
import { useQuery } from "@tanstack/react-query";

import { TrackApi } from "../api/trackApi";
import type { TrackRelationModel } from "../models/trackModel";
import type { ApiListResponse } from "../../../services/api/types";
import { Pagination } from "../../../services/ui/Pagination";

// Import component css:
import "./BoxContainer.css";
import "./Tracks.css";

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

  // {data.page_results.map((track) => (
  //   <li key={track.pk}>{track.name} {track.total_distance ?? 0} m</li>
  // ))}

  return (
    <div className="box-container-objects">
      <div className="box-container-heder">
        <h2></h2>
      </div>
      
      <div className="box-container-body">
        {data.page_results.map((track) => (
          <a href="card1" className="container-card">
            <div className="container-card-image">
              <></>
            </div>
            <div className="container-card-content">
              <div className="container-card-title card-content-element">
                <h3>{track.name}</h3>
              </div>
              <div className="container-card-properties card-content-element">
                <div className="container-card-property">
                  <span>{track.category.label}</span>
                </div>
                <div className="container-card-property">
                  <span>{track.category_specific_difficulty.label}</span>
                </div>
                <div className="container-card-property">
                  <span>{track.total_distance ?? 0} m</span>
                </div>
                <div className="container-card-property">
                  <span>{track.elevation_gain ?? 0} m</span>
                </div>
              </div>
              <div className="container-card-description card-content-element">
                <p>{track.snippet}</p>
              </div>
              <div className="container-card-extra card-content-element">
                <div className="container-card-extra-item">
                  <span>4.5</span>
                </div>
                <div className="container-card-extra-item">
                  <span>6h 30m</span>
                </div>
                <div className="container-card-extra-item">
                  <span>1232</span>
                </div>
              </div>
            </div>
          </a>
        ))}
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
