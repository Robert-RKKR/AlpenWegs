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
 * POI Model (expanded)
 * ========================================================= */
export type PoiRelationModel = {
    pk: string;
    url: string;

    name: string;
    slug: string;
    snippet: string | null;
    description: string | null;

    location: string | null;
    elevation: number | null;

    created: string;
    updated: string;

    is_public: boolean;
    creator: string;

    transport_description: string | null;

    category: TrackCategoryModel;
    region: string;
};
