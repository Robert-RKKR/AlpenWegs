// Application imports:
import type { ObjectDetailsSchema } from "../types";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

// React imports:
import { useState } from "react";

// Import component css:
import "./ObjectDetails.css";

type Props<T> = {
  queryKey: (id: string) => unknown[];
  queryFn: (id: string) => Promise<T>;
  mapDetails: (data: T) => ObjectDetailsSchema;
};

export function ObjectDetails<T>({ queryKey, queryFn, mapDetails }: Props<T>) {
  const { id } = useParams<{ id: string }>();
  
  const [activeChapter, setActiveChapter] = useState(0);

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
      <div className="object-details-title object-details-card card-box">
        <h1>{details.title}</h1>
      </div>

      <div className="object-details-container">

        <div className="object-details-left">

          <div className="object-details-gallery object-details-card card-box">
            {details.image && <img src={details.image} alt={details.title} />}
          </div>

          <div className="object-details-chapters object-details-card card-box">
            {details.chapters && details.chapters.length > 0 && (
              <div className="object-details-tabs">
                {details.chapters.map((chapter, index) => (
                  <button
                    key={index}
                    className={`object-details-tab ${
                      index === activeChapter ? "active" : ""
                    }`}
                    onClick={() => setActiveChapter(index)}
                    type="button"
                  >
                    {chapter.title}
                  </button>
                ))}
              </div>
            )}

            {details.chapters && details.chapters[activeChapter] && (
              <div className="object-details-tab-content">
                {details.chapters[activeChapter].properties.map((p, j) => (
                  <div key={j} className="object-details-property-row">
                    <span className="label">{p.label}</span>
                    <span className="value">{p.value}</span>
                  </div>
                ))}
              </div>
            )}

          </div>

        </div>

        <div className="object-details-right">
          {details.properties && (
            <div className="object-details-properties object-details-card card-box">
              {details.properties.map((p, i) => (
                <div key={i}>
                  <strong>{p.label}:</strong> {p.value}
                </div>
              ))}
            </div>
          )}
        </div>

      </div>
    </div>
  );
}
