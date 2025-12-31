// React imports:
import { useState } from "react";

// Import component css:
import "./ImageLoader.css";

type ImageLoaderProps = {
  src?: string | null;
  alt: string;
  fallback?: string;
};

export function ImageLoader({
  src,
  alt,
  fallback = "/empty.jpg",
}: ImageLoaderProps) {
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState(false);

  const imageSrc = !src || error ? fallback : src;

  return (
    <div className={"image-loader-container"}>
      {!loaded && (
        <div className="image-loader-spinner" />
      )}

      <img
        src={imageSrc}
        alt={alt}
        className={`image-loader-img ${loaded ? "visible" : "hidden"}`}
        onLoad={() => setLoaded(true)}
        onError={() => {
          setError(true);
          setLoaded(true);
        }}
        loading="lazy"
      />
    </div>
  );
}
