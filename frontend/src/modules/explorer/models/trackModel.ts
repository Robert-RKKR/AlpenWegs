/* Track Representation Model */
export type TrackRepresentationModel = {
    pk: string;
    url: string;
    name: string;
};

/* Track Relation Model */
export type TrackRelationModel = TrackRepresentationModel & {
    snippet: string | null;
    total_distance: number;
    elevation_gain: number;
    is_public: boolean;
    start_time: string | null;
    end_time: string | null;
    moving_time: number | null;
    total_time: number | null;
    average_speed: number | null;
    maximum_speed: number | null;
    elevation_loss: number | null;
    highest_elevation: number | null;
    lowest_elevation: number | null;
    verified: boolean | null;
    score: number | null;
};

/* Track Detailed Model */
// export type TrackDetailedModel = TrackRelationModel & {
// };
