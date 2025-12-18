import { useEffect, useRef, useState } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { CircleUser, LogOut } from "lucide-react";

import { useAuthStore } from "../../stores/authStore";
import { logout } from "../../modules/profiles/api/authApi";

import "./UserMenu.css";

export function UserMenu() {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  const { isAuthenticated, user, refreshToken, clearAuth } =
    useAuthStore();

  // Close menu on outside click
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (ref.current && !ref.current.contains(event.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  async function handleLogout() {
    try {
      if (refreshToken) {
        await logout(refreshToken);
      }
    } finally {
      clearAuth();
      setOpen(false);
      navigate("/auth/login");
    }
  }

  return (
    <div className="user-menu-wrapper" ref={ref}>
      <button
        className="user-menu-trigger"
        onClick={() => setOpen((v) => !v)}
        aria-label="User menu"
      >
        <CircleUser />
      </button>

      {open && (
        <div className="user-menu">
          {!isAuthenticated && (
            <>
              <NavLink
                to="/auth/login"
                className="user-menu-item"
                onClick={() => setOpen(false)}
              >
                Log in
              </NavLink>
            </>
          )}

          {isAuthenticated && user && (
            <>
              <div className="user-menu-user">
                <strong>
                  {user.first_name} {user.last_name}
                </strong>
                <span>{user.email}</span>
              </div>

              <NavLink
                to="/auth/profile"
                className="user-menu-item"
                onClick={() => setOpen(false)}
              >
                Profile
              </NavLink>

              <button
                className="user-menu-item logout"
                onClick={handleLogout}
              >
                <LogOut size={16} />
                Log out
              </button>
            </>
          )}
        </div>
      )}
    </div>
  );
}
