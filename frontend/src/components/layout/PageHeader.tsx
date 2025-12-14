// Import application components:
import { RkLogo } from "../../assets/logo/RkLogo";

// Import React components:
import { NavLink } from "react-router-dom";
import { CircleUser } from "lucide-react";

// Import component css:
import "./PageHeader.css";


export function PageHeader() {
  return (
    <header className="page-header">
      {/* LEFT */}
      <div className="header-left">
        <div className="header-section">
          <div className="header-logo">
            <NavLink to="/" aria-label="AlpenWegs Homepage">
              <RkLogo />
            </NavLink>
          </div>
        </div>

        <div className="header-section">
          <nav className="header-menu">
            <NavLink to="/explorer" className="header-menu-item">
              Plans
            </NavLink>
            <NavLink to="/events" className="header-menu-item">
              Events
            </NavLink>
            <NavLink to="/compendium" className="header-menu-item">
              Compendium
            </NavLink>
          </nav>
        </div>
      </div>

      {/* RIGHT */}
      <div className="header-right">
        <div className="header-section">
          <div className="header-search">
            <input type="text" placeholder="Search..." />
          </div>
        </div>

        <div className="header-section">
          <div className="header-user">
            <NavLink to="/profile">
              <CircleUser />
            </NavLink>
          </div>
        </div>
      </div>
    </header>
  );
}
