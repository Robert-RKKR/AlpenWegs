// React import:
import { useAuthStore } from "../../../../stores/authStore";
import { useQuery } from "@tanstack/react-query";

// Application import:
import { fetchUserProfile } from "../../api/userApi";
import type { UserModel } from "../../api/userApi";

// Import component css:
import "./UserPage.css";

export function UserPage() {
  const user = useAuthStore((s) => s.user);

  // Auth guard
  if (!user?.pk) {
    return <div>Not authenticated</div>;
  }

  const {
    data,
    isLoading,
    error,
  } = useQuery<UserModel>({
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
    <div className="profile-container">
      <div className="profile-menu">
        <h2>User Profile</h2>
      </div>

      <div className="profile-content">
        <div className="profile-details-item">
          <div className="profile-details-label">ID</div>
          <div className="profile-details-value">{data.pk}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">Email</div>
          <div className="profile-details-value">{data.email}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">First name</div>
          <div className="profile-details-value">{data.first_name}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">Last name</div>
          <div className="profile-details-value">{data.last_name}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">Phone number</div>
          <div className="profile-details-value">{data.phone_number || "No phone number data"}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">Birthday</div>
          <div className="profile-details-value">{data.birthday || "No birthday data"}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">User created</div>
          <div className="profile-details-value">{data.created}</div>
        </div>

        <div className="profile-details-item">
          <div className="profile-details-label">Last login</div>
          <div className="profile-details-value">{data.last_login}</div>
        </div>
      </div>
    </div>
  );
}
