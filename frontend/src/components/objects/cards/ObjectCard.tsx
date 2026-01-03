// Application imports:
import { ImageLoader } from "../../elements/imageLoader/ImageLoader";
import type { ObjectCardProps } from "../types";

// React imports:
import { Link } from "react-router-dom";

// Import component css:
import "./ObjectCard.css";

// ObjectCard component:
export function ObjectCard({
  href,
  image,
  title,
  properties = [],
  description,
  extras = [],
}: ObjectCardProps) {

  return (
    <Link to={href} className="objects-card card-box">
      {/* Image – single value */}
      <div className="objects-card-image">
        <ImageLoader
          src={image as string}
          alt={title}
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
    </Link>
  );
}
