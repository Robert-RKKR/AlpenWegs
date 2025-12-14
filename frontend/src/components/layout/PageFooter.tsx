// Import React components:
import { NavLink } from "react-router-dom";
import { CircleUser } from "lucide-react";

// Import component css:
import "./PageFooter.css";

export function PageFooter() {
  return (
    <footer className="page-footer">
      <div className="footer-menu">
        <NavLink to="/home" className="footer-menu-item">
          Home
        </NavLink>
        <NavLink to="/plans" className="footer-menu-item">
          Plans
        </NavLink>
        <NavLink to="/records" className="footer-menu-item">
          Records
        </NavLink>
        <NavLink to="/events" className="footer-menu-item">
          Events
        </NavLink>
        <NavLink to="/compendium" className="footer-menu-item">
          Compendium
        </NavLink>
      </div>
      <div className="footer-submenu">
        <p className="footer-submenu-item">© 2025 AlpenWegs</p>
      </div>
    </footer>
  );
}