/* =========================================================
 * Photo File Model
 * ========================================================= */
export type PhotoRelationModel = {
    pk: string;
    url: string;

    name: string;
    slug: string;
    snippet: string | null;

    created: string;
    updated: string;

    is_public: boolean;
    creator: string;

    format: string;
    path: string;
};
