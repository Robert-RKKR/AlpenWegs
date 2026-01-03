// Application imports:
import { ImageCarousel } from "../../elements/imageCarousel/ImageCarousel";
import { BaseApi } from "../../../services/api/baseApi";
import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

// React imports:
import { Link } from "react-router-dom";
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
  routes: {
    edit: string;
  };
  title: {
    key: string;
    label?: string;
    value: string[];
  };
  image?: {
    key: string;
    label?: string;
    value: string[];
  };
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
export function ObjectRetrieveComponent<T>({ config }: Props<T>) {
  const { id } = useParams<{ id: string }>();
  const [activeChapter, setActiveChapter] = useState(0);

  const { data, isLoading, error } = useQuery<T>({
    queryKey: [config.api.listUrl, id],
    queryFn: () =>
      BaseApi.retrieve<T>(`${config.api.listUrl}${id}/`),
    enabled: !!id,
  });

  const resolvedTitle =
    data && config.title
      ? resolvePath(data, config.title.value)
      : undefined;

  const resolvedImages =
  data && config.image
    ? resolvePath(data, config.image.value)
    : undefined;

  return (
    <div className="object-retrieve">
      {/* Title */}
      {!isLoading && !error && resolvedTitle && (
        <div className="object-retrieve-title object-retrieve-card card-box">
          <h1>{resolvedTitle}</h1>
        </div>
      )}

      {/* Loading */}
      {isLoading && (
        <div className="object-retrieve-card card-box">
          <p>Loading…</p>
        </div>
      )}

      {/* Error */}
      {!isLoading && error && (
        <div className="object-retrieve-card card-box">
          <p>Failed to load data</p>
        </div>
      )}

      {/* Data */}
      {!isLoading && !error && data && (
        <div className="object-retrieve-container">
          {/* Left column */}
          <div className="object-retrieve-left">
            {/* Image */}
            {Array.isArray(resolvedImages) && resolvedImages.length > 0 && (
              <div className="object-retrieve-card card-box">
                <ImageCarousel
                  height={500}
                  images={resolvedImages.map((item) => ({
                    src: item.photo?.path ?? null,
                    alt: String(resolvedTitle ?? ""),
                  }))}
                />
              </div>
            )}

            {/* Chapters */}
            {config.chapters && config.chapters.length > 0 && (
              <div className="object-retrieve-chapters object-retrieve-card card-box">
                <div className="object-retrieve-tabs">
                  {config.chapters.map((chapter, index) => (
                    <button
                      key={index}
                      className={`object-retrieve-tab ${
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
                  <div className="object-retrieve-content">
                    {config.chapters[activeChapter].properties.map(
                      (p, j) => (
                        <div
                          key={j}
                          className="object-retrieve-property-row"
                        >
                          <span className="label">{p.label}:</span>
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
          <div className="object-retrieve-right">
            {config.properties && (
              <div className="object-retrieve-properties object-retrieve-card card-box">
                {config.properties.map((p, i) => (
                  <div key={i}>
                    <span className="label">{p.label}:</span>
                    <span className="value">
                      {`${resolvePath(data, p.value) ?? ""}${p.suffix ?? ""}`}
                    </span>
                  </div>
                ))}
              </div>
            )}
            {data && id && (
              <div className="object-retrieve-card card-box">
                <Link
                  to={`${config.routes.edit}/${id}/edit`}
                  className="object-retrieve-button"
                >
                  Edit
                </Link>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
