/* =========================================================
 * User (Creator) Model – detailed
 * ========================================================= */
export type UserGenderModel = {
    value: number | null;
    label: boolean;
};

export type UserRelationModel = {
    pk: string;
    url: string;

    created: string;
    updated: string;
    last_login: string | null;

    is_superuser: boolean;
    is_active: boolean;
    is_staff: boolean;

    username: string;
    email: string;

    first_name: string;
    middle_name: string | null;
    last_name: string;

    phone_number: string | null;
    birthday: string | null;

    gender: UserGenderModel;

    weight: number | null;
    height: number | null;
    bmi: number | null;

    location_name: string | null;
    location: string | null;

    password_to_change: boolean;
};
