// Application imports:
import type { ObjectDetailsSchema } from "../types";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

// Import component css:
import "./ObjectDetails.css";

type Props<T> = {
  queryKey: (id: string) => unknown[];
  queryFn: (id: string) => Promise<T>;
  mapDetails: (data: T) => ObjectDetailsSchema;
};

export function ObjectDetails<T>({
  queryKey,
  queryFn,
  mapDetails,
}: Props<T>) {
  const { id } = useParams<{ id: string }>();

  const { data, isLoading } = useQuery({
    queryKey: queryKey(id!),
    queryFn: () => queryFn(id!),
    enabled: !!id,
  });

  if (isLoading || !data) {
    return <div>Loading…</div>;
  }

  const details = mapDetails(data);

  return (
    <div className="object-details">
      {details.image && (
        <img src={details.image} alt={details.title} />
      )}

      <h1>{details.title}</h1>

      {details.properties && (
        <div className="object-details-properties">
          {details.properties.map((p, i) => (
            <div key={i}>
              <strong>{p.label}:</strong> {p.value}
            </div>
          ))}
        </div>
      )}

      {details.chapters?.map((chapter, i) => (
        <section key={i}>
          <h2>{chapter.title}</h2>
          {chapter.properties.map((p, j) => (
            <div key={j}>
              <strong>{p.label}:</strong> {p.value}
            </div>
          ))}
        </section>
      ))}
    </div>
  );
}
