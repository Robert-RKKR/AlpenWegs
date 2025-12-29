/* Base Track Representation */
export type TrackRepresentationModel = {
    pk: string;
    url: string;
    name: string;
};

/* Track Category Model */
export type TrackCategoryModel = {
    value: number;
    label: string;
    icon: string;
    description: string;
    depend: number | null;
};

/* Track Difficulty Model */
export type TrackDifficultyModel = {
    value: number;
    label: string;
};

/* Track Relation Model */
export type TrackRelationModel = TrackRepresentationModel & {
    snippet: string | null;

    total_distance: number;
    elevation_gain: number;
    elevation_loss: number | null;

    highest_elevation: number | null;
    lowest_elevation: number | null;

    start_time: string | null;
    end_time: string | null;
    moving_time: number | null;
    total_time: number | null;

    average_speed: number | null;
    maximum_speed: number | null;

    is_public: boolean;
    verified: boolean | null;
    score: number | null;

    category: TrackCategoryModel;
    category_specific_difficulty: TrackDifficultyModel;
};

/* Track Detailed Model */
// export type TrackDetailedModel = TrackRelationModel & {
// };
