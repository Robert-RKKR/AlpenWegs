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
    <div>
      <h1>Profile</h1>
      <br />
      <p>
        <strong>ID:</strong> {data.pk}
      </p>
      <br />
      <p>
        <strong>Email:</strong> {data.email}
      </p>
      <br />
      <p>
        <strong>First name:</strong> {data.first_name}
      </p>
      <br />
      <p>
        <strong>Last name:</strong> {data.last_name}
      </p>
      <br />
      <p>
        <strong>Last login:</strong> {data.last_login}
      </p>
    </div>
  );
}
