// Imports:
import { Box, Image, Loader, Center } from "@mantine/core";
import { useState } from "react";

type ImageLoaderProps = {
  src?: string | null;
  alt: string;
  fallback?: string;

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
  radius = "md",
}: ImageLoaderProps) {
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState(false);

  const imageSrc = !src || error ? fallback : src;

  return (
    <Box
      pos="relative"
      h={height}
      w={width}
      style={{ borderRadius: radius, overflow: "hidden" }}
    >
      {/* Loader overlay */}
      {!loaded && (
        <Center
          pos="absolute"
          inset={0}
          style={{ zIndex: 1 }}
        >
          <Loader size="sm" />
        </Center>
      )}

      {/* Image */}
      <Image
        src={imageSrc}
        alt={alt}
        fit={fit}
        height="100%"
        width="100%"
        radius={radius}
        loading="lazy"
        onLoad={() => setLoaded(true)}
        onError={() => {
          setError(true);
          setLoaded(true);
        }}
      />
    </Box>
  );
}
