// Application imports:
import { ImageLoader } from "../imageLoader/ImageLoader";
import { useEffect, useState } from "react";

// Properties:
type ImageCarouselItem = {
  src: string | null;
  alt: string;
};

type ImageCarouselProps = {
  images: ImageCarouselItem[];
  height?: number;
};

// ImageCarousel component:
export function ImageCarousel({
  images,
  height = 360,
}: ImageCarouselProps) {
  const [index, setIndex] = useState(0);
  const [open, setOpen] = useState(false);

  if (!Array.isArray(images) || images.length === 0) {
    return null;
  }

  const prev = () =>
    setIndex((i) => (i === 0 ? images.length - 1 : i - 1));

  const next = () =>
    setIndex((i) => (i === images.length - 1 ? 0 : i + 1));

  const close = () => setOpen(false);

  // ESC key support
  useEffect(() => {
    if (!open) return;

    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") prev();
      if (e.key === "ArrowRight") next();
    };

    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <>
      {/* Carousel */}
      <div className="image-carousel" style={{ height }}>
        {images.map((img, i) => (
          <div
            key={i}
            className={`image-carousel-slide ${
              i === index ? "active" : ""
            }`}
            onClick={() => setOpen(true)}>
            <ImageLoader src={img.src} alt={img.alt} />
          </div>
        ))}

        {images.length > 1 && (
          <>
            <button type="button" className="image-carousel-btn prev" onClick={prev}>
              ‹
            </button>
            <button type="button" className="image-carousel-btn next" onClick={next}>
              ›
            </button>
          </>
        )}
      </div>

      {/* Lightbox */}
      {open && (
        <div className="image-carousel-lightbox" onClick={close}>
          <div
            className="image-carousel-lightbox-content"
            onClick={(e) => e.stopPropagation()}
          >
            <button className="image-carousel-close" onClick={close} type="button">
              ✕
            </button>
            <ImageLoader src={images[index].src} alt={images[index].alt}/>
            {images.length > 1 && (
              <>
                <button type="button" className="image-carousel-btn prev" onClick={prev}>
                  ‹
                </button>
                <button type="button" className="image-carousel-btn next" onClick={next}>
                  ›
                </button>
              </>
            )}
          </div>
        </div>
      )}
    </>
  );
}
