// Import application components:
import { RkLogo } from "../../assets/logo/RkLogo";
import { UserMenu } from "../other/UserMenu";

// Import React components:
import { NavLink } from "react-router-dom";

// Import component css:
import "./PageHeader.css";

// Main Component Function:
export function PageHeader() {
  
  return (
    <header className="page-header">
      
      {/* Header Left Section */}
      <div className="header-left">
        
        {/* Header Logo Section */}
        <div className="header-section">
          <div className="header-logo">
            <NavLink to="/" aria-label="AlpenWegs Homepage">
              <RkLogo />
            </NavLink>
          </div>
        </div>

        {/* Header Menu Section */}
        <div className="header-section">
          <nav className="header-menu">
            <NavLink to="/plans" className="header-menu-item">
              Plans
            </NavLink>
            <NavLink to="/explorer/tracks" className="header-menu-item">
              Records
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

      {/* Header Right Section */}
      <div className="header-right">

        {/* Header Search Section */}
        <div className="header-section">
          <div className="header-search">
            <input type="text" placeholder="Search..." />
          </div>
        </div>

        {/* Header User Section */}
        <div className="header-section">
          <div className="header-user">
            <UserMenu />
          </div>
        </div>
        
      </div>
    </header>
  );
}
