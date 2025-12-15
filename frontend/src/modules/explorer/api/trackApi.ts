import { BaseApi } from "../../../services/api/baseApi";
import type {
  TrackRepresentationModel,
  TrackRelationModel,
} from "../models/trackModel";

type ListParams = Record<string, unknown>;

export const TrackApi = {
  /* ---------- Representation (minimal) ---------- */
  list: (params?: ListParams) =>
    BaseApi.list<TrackRepresentationModel>(
      "/api/explorers/track/representation/",
      params
    ),

  /* ---------- Relation (list-friendly) ---------- */
  light: (params?: ListParams) =>
    BaseApi.list<TrackRelationModel>(
      "/api/explorers/track/",
      params
    ),
};