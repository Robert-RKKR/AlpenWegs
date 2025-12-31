// Import applicable types:
import type { ObjectCardProps } from "../types";

// Import component css:
import "./ObjectCard.css";

// React imports:
import { useState } from "react";

// ObjectCard component:
export function ObjectCard({
  href,
  image,
  title,
  properties = [],
  description,
  extras = [],
}: ObjectCardProps) {

  // State to track if image has loaded:
  const [loaded, setLoaded] = useState(false);

  return (
    <a href={href} className="objects-card">
      {/* Image – single value */}
      <div className="objects-card-image">
        <img
          src={loaded && image ? image : "/empty.jpg"}
          alt={title}
          onLoad={() => setLoaded(true)}
          onError={(e) => {
            (e.currentTarget as HTMLImageElement).src = "/empty.jpg";
          }}
        />
      </div>

      <div className="objects-card-content">
        {/* Title – single value */}
        <div className="objects-card-title objects-card-element">
          <h3>{title}</h3>
        </div>

        {/* Properties – list of values */}
        {properties.length > 0 && (
          <div className="objects-card-properties objects-card-element">
            {properties.map((value, index) => (
              <div
                key={index}
                className="objects-card-property"
              >
                <span>{value}</span>
              </div>
            ))}
          </div>
        )}

        {/* Description – single value */}
        {description && (
          <div className="objects-card-description objects-card-element">
            <p>{description}</p>
          </div>
        )}

        {/* Extras – list of values */}
        {extras.length > 0 && (
          <div className="objects-card-extra objects-card-element">
            {extras.map((value, index) => (
              <div
                key={index}
                className="objects-card-extra-item"
              >
                <span>{value}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </a>
  );
}
