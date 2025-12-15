// Import React components:
import { NavLink } from "react-router-dom";
import { CircleUser } from "lucide-react";

// Import component css:
import "./UserProfile.css";

// Main Component Function:
export function UserProfile() {
  return (
    <div className="user-profile-container">

        <div className="user-profile-menu">

            <div className="user-profile-logo">
                <CircleUser />
                <h2 className="user-profile-name">Robert Tadeusz Kucharski</h2>
            </div>

            <div className="user-profile-menu">
                <NavLink to="/auth/profile" className="user-profile-menu-item">Details</NavLink>
                <NavLink to="/auth/dashboard" className="user-profile-menu-item">Dashboard</NavLink>
                <NavLink to="/auth/cards" className="user-profile-menu-item">Cards</NavLink>
            </div>

        </div>

        <div className="user-profile-content">
            
        </div>

    </div>
  );
}