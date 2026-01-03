// Application imports:
import { BaseApi } from "../../../services/api/baseApi";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

// React imports:
import { useState } from "react";

// Import component css:
import "./RetrieveComponent.css";

// Helpers functions:
function resolvePath(obj: any, path?: string[]) {
  if (!path) return undefined;
  return path.reduce((acc, key) => acc?.[key], obj);
}

// Properties:
type ObjectRetrieveConfig = {
  api: {
    listUrl: string;
  };
  header?: {
    title?: string;
  };
  image?: string[];
  properties?: {
    key: string;
    label: string;
    value: string[];
    suffix?: string;
  }[];
  chapters?: {
    title: string;
    properties: {
      key: string;
      label: string;
      value: string[];
      suffix?: string;
    }[];
  }[];
};

type Props<T> = {
  config: ObjectRetrieveConfig;
};

// ObjectRetrieveComponent component:
export function ObjectRetrieveComponent<T>({
  config,
}: Props<T>) {
  const { id } = useParams<{ id: string }>();
  const [activeChapter, setActiveChapter] = useState(0);

  const { data, isLoading, error } = useQuery<T>({
    queryKey: [config.api.listUrl, id],
    queryFn: () =>
      BaseApi.retrieve<T>(`${config.api.listUrl}${id}/`),
    enabled: !!id,
  });

  return (
    <div className="object-details">
      <div className="object-details-title object-details-card card-box">
        <h1>{config.header?.title}</h1>
      </div>

      {/* Loading / Error */}
      {isLoading && (
        <div className="object-details-card card-box">
          <p>Loading…</p>
        </div>
      )}

      {!isLoading && error && (
        <div className="object-details-card card-box">
          <p>Failed to load data</p>
        </div>
      )}

      {/* Data */}
      {!isLoading && !error && data && (
        <div className="object-details-container">
          {/* Left column */}
          <div className="object-details-left">
            {/* Image */}
            {config.image && (
              <div className="object-details-gallery object-details-card card-box">
                {resolvePath(data, config.image) && (
                  <img
                    src={resolvePath(data, config.image)}
                    alt={config.header?.title}
                  />
                )}
              </div>
            )}

            {/* Chapters */}
            {config.chapters && config.chapters.length > 0 && (
              <div className="object-details-chapters object-details-card card-box">
                <div className="object-details-tabs">
                  {config.chapters.map((chapter, index) => (
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

                {config.chapters[activeChapter] && (
                  <div className="object-details-tab-content">
                    {config.chapters[activeChapter].properties.map(
                      (p, j) => (
                        <div
                          key={j}
                          className="object-details-property-row"
                        >
                          <span className="label">{p.label}</span>
                          <span className="value">
                            {`${resolvePath(data, p.value) ?? ""}${p.suffix ?? ""}`}
                          </span>
                        </div>
                      ),
                    )}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Right column */}
          <div className="object-details-right">
            {config.properties && (
              <div className="object-details-properties object-details-card card-box">
                {config.properties.map((p, i) => (
                  <div key={i}>
                    <strong>{p.label}:</strong>{" "}
                    {`${resolvePath(data, p.value) ?? ""}${p.suffix ?? ""}`}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
