// React imports:
import { useState } from "react";

// Components:
import { StateLoader } from "../stateLoader/StateLoader";

// Import component css:
import "./ImageLoader.css";

type ImageLoaderProps = {
  src?: string | null;
  alt: string;
  fallback?: string;

  /** NEW */
  height?: number | string;
  width?: number | string;
  fit?: "cover" | "contain";
  radius?: number | string;
};

export function ImageLoader({
  src,
  alt,
  fallback = "/empty.jpg",

  height = 160,
  width = "100%",
  fit = "cover",
  radius,
}: ImageLoaderProps) {
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState(false);

  const imageSrc = !src || error ? fallback : src;

  return (
    <div
      className="image-loader-container"
      style={{
        height,
        width,
        borderRadius: radius,
      }}
    >
      {!loaded && (
        <div className="image-loader-overlay">
          <StateLoader />
        </div>
      )}

      <img
        src={imageSrc}
        alt={alt}
        className={`image-loader-img ${loaded ? "visible" : "hidden"}`}
        style={{
          objectFit: fit,
          height: "100%",
          width: "100%",
          borderRadius: radius,
        }}
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
