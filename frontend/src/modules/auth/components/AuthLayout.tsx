import { NavLink, Outlet } from "react-router-dom";
import { CircleUser } from "lucide-react";
import { useAuthStore } from "../../../stores/authStore";
import { useQuery } from "@tanstack/react-query";
import { fetchUserProfile } from "../api/profileApi";
import type { UserProfile } from "../api/profileApi";

import "./UserProfile.css";

export function AuthLayout() {
  const user = useAuthStore((s) => s.user);

  if (!user?.pk) {
    return <div>Not authenticated</div>;
  }

  const {
    data,
    isLoading,
    error,
  } = useQuery<UserProfile>({
    queryKey: ["user-profile", user.pk],
    queryFn: () => fetchUserProfile(user.pk),
  });

  if (isLoading) {
    return <div>Loading profile…</div>;
  }

  if (error || !data) {
    return <div>Failed to load profile</div>;
  }

  return (
    <div className="user-profile-container">

      {/* Left menu */}
      <aside className="user-profile-menu">
        <div className="user-profile-logo">
          <CircleUser />
          <h2 className="user-profile-name">
            {data.first_name} {data.last_name}
          </h2>
        </div>

        <nav className="user-profile-menu">
          <NavLink to="/auth/profile" className="user-profile-item">
            Details
          </NavLink>
          <NavLink to="/auth/dashboard" className="user-profile-item">
            Dashboard
          </NavLink>
          <NavLink to="/auth/cards" className="user-profile-item">
            Cards
          </NavLink>
        </nav>
      </aside>

      {/* Page-specific content */}
      <main className="user-profile-content">
        <Outlet context={data} />
      </main>

    </div>
  );
}
