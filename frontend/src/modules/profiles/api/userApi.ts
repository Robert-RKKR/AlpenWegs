import { apiClient } from "../../../services/api/client";

export type UserGender = {
  value: string | null;
  label: string | boolean | null;
};

export type UserModel = {
  pk: string;
  url: string;
  created: string;
  updated: string;
  last_login: string;
  is_superuser: boolean;
  is_active: boolean;
  is_staff: boolean;
  password_to_change: boolean;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  middle_name: string | null;
  phone_number: string | null;
  birthday: string | null;
  gender: UserGender | null;
  weight: number | null;
  height: number | null;
  bmi: number | null;
  location_name: string | null;
  location: unknown | null;
};

export async function fetchUserProfile(
  userPk: string
): Promise<UserModel> {
  const response = await apiClient.get(
    `/api/profiles/user/${userPk}/`
  );
  return response.data.page_results;
}
