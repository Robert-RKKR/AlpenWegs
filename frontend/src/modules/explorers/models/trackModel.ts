
import type { PoiRelationModel } from "../../compendiums/models/poiModel";
import type { UserRelationModel } from "../../profiles/models/userModel";
import type { PhotoRelationModel } from "../../assets/models/photoModel";
import type { FileRelationModel } from "../../assets/models/fileModel";

/* =========================================================
 * Track Category Model
 * ========================================================= */
export type TrackCategoryModel = {
    value: number;
    label: string;
    icon: string;
    description: string;
    depend: number | null;
};

/* =========================================================
 * Track Difficulty Model
 * ========================================================= */
export type TrackDifficultyModel = {
    value: number;
    label: string;
};

/* =========================================================
 * GeoJSON
 * ========================================================= */
export type GeoJsonLineStringModel = {
    type: "LineString";
    coordinates: [number, number, number?][];
};

/* =========================================================
 * Elevation Graph
 * ========================================================= */
export type ElevationGraphPointModel = {
    index: number;
    elevation: number;
};

/* =========================================================
 * Track Relation Model (FULL – API aligned)
 * ========================================================= */
export type TrackRelationModel = {
    /* ---------- Identification ---------- */
    pk: string;
    url: string;
    name: string;
    slug: string;

    /* ---------- Descriptive ---------- */
    snippet: string | null;

    /* ---------- Category ---------- */
    category: TrackCategoryModel;
    category_specific_difficulty: TrackDifficultyModel;

    /* ---------- Time ---------- */
    start_time: string | null;
    end_time: string | null;
    moving_time: number | null;
    stop_time: number | null;
    total_time: number | null;

    /* ---------- Distance & Elevation ---------- */
    total_distance: number;
    elevation_gain: number;
    elevation_loss: number | null;
    elevation: number | null;

    highest_elevation: number | null;
    lowest_elevation: number | null;

    average_grade: number | null;
    highest_grade: number | null;

    /* ---------- Speed ---------- */
    average_speed: number | null;
    moving_average_speed: number | null;
    maximum_speed: number | null;

    ascent_average_speed: number | null;
    descent_average_speed: number | null;
    maximum_ascent_speed: number | null;
    maximum_descent_speed: number | null;

    /* ---------- Pace ---------- */
    pace_average: number | null;
    pace_best: number | null;

    /* ---------- Heart & Fitness ---------- */
    average_heart_rate: number | null;
    maximum_heart_rate: number | null;
    minimum_heart_rate: number | null;

    calories_burned: number | null;
    steps_count: number | null;

    /* ---------- Conditions ---------- */
    weather_conditions: string | null;
    temperature_average: number | null;
    equipment_used: string | null;

    /* ---------- Movement ---------- */
    moving_ratio: number | null;
    total_points: number;

    /* ---------- Location ---------- */
    location: string | null;

    start_poi: string | null;
    end_poi: string | null;

    /* ---------- Relations ---------- */
    journey: string | null;
    route: string | null;

    pois: string[];

    /* ---------- Media ---------- */
    photos: string[];
    primary_photo: string | null;

    /* ---------- Flags / Track Type ---------- */
    snow_track: boolean;
    night_track: boolean;
    fog_track: boolean;
    rain_track: boolean;
    hot_weather_track: boolean;
    cold_weather_track: boolean;
    windy_track: boolean;

    group_track: boolean;
    organized_track: boolean;
    leader_track: boolean;
    guided_tour_track: boolean;

    backpacking_track: boolean;
    fast_hike_track: boolean;
    training_track: boolean;
    exploration_track: boolean;

    hazardous_track: boolean;

    /* ---------- Safety ---------- */
    injury_occurred: boolean;
    rescue_assistance: boolean;

    /* ---------- Meta ---------- */
    created: string;
    updated: string;

    creator: string;

    is_public: boolean;
    verified: boolean | null;

    score: number | null;
    similarity_index: number | null;

    user_notes: string | null;

    comment_count: number;
    visit_count: number;
    download_count: number;

    track_types: string[] | null;
};

/* Track to Photo Model */
export type TrackPhotoRelationModel = {
    id: string;

    created: string;
    updated: string;

    track: string;
    photo: PhotoRelationModel;

    is_primary: boolean;
};

/* =========================================================
 * Track Detailed Model
 * ========================================================= */
export type TrackDetailedModel = TrackRelationModel & {
    /* ---------- Creator (expanded) ---------- */
    creator: UserRelationModel;

    /* ---------- GPX ---------- */
    gpx_data: FileRelationModel | null;

    /* ---------- Geometry ---------- */
    geojson: GeoJsonLineStringModel | null;

    elevation_graph: ElevationGraphPointModel[];

    /* ---------- POIs ---------- */
    start_poi: PoiRelationModel | null;
    end_poi: PoiRelationModel | null;

    /* ---------- Photos ---------- */
    photos: TrackPhotoRelationModel[];
};
