// Application imports:
import { BaseApi } from "../../../services/api/baseApi";
import type {
  TrackRepresentationModel,
  TrackRelationModel,
  TrackDetailedModel,
} from "../models/trackModel";

// List parameters type:
type ListParams = Record<string, unknown>;

// TrackApi object:
export const TrackApi = {
  /* Representation (minimal) */
  list: (params?: ListParams) =>
    BaseApi.list<TrackRepresentationModel>(
      "/api/explorers/track/representation/",
      params
    ),

  /* Relation (list-friendly) */
  light: (params?: ListParams) =>
    BaseApi.list<TrackRelationModel>(
      "/api/explorers/track/",
      params
    ),

  /* Detailed (single object) */
  retrieve: (id: string) =>
    BaseApi.retrieve<TrackDetailedModel>(
      `/api/explorers/track/${id}/`
    ),
};