// Import React components:
import { NavLink } from "react-router-dom";
import { ShieldAlert } from "lucide-react";

// Import component css:
import "./NotFoundPage.css";

// Main Page Function:
export function NotFoundPage() {
  return (
    <div className="box-component-pagination not-found-page">
      <ShieldAlert className="not-found-icon" />
      <h2 className="not-found-title">404</h2>
      <p className="not-found-description">The page you are looking for does not exist.</p>
      <NavLink to="/" style={{ textDecoration: "underline" }} className="not-found-link">
        Go back to Home
      </NavLink>
    </div>
  );
}
