import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import { login } from "../../api/authApi";
import { useAuthStore } from "../../../../stores/authStore";

// Import application components:
import { RkLogo } from "../../../../assets/logo/RkLogo";

// Import React components:
import { NavLink } from "react-router-dom";

// Import component css:
import "./LoginPage.css";

export function LoginPage() {
  const navigate = useNavigate();
  const setAuth = useAuthStore((s) => s.setAuth);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const { user, access, refresh } = await login({
        email,
        password,
      });

      setAuth(user, access, refresh);
      navigate("/auth/profile");
    } catch (err) {
      if (axios.isAxiosError(err)) {
        setError(
          err.response?.data?.page_error?.error_message ??
          "Login failed"
        );
      } else {
        setError("Unexpected error occurred");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="login-container" onSubmit={handleSubmit}>

      <div className="login-card">
        <div className="login-logo">
          <NavLink to="/" aria-label="AlpenWegs Homepage">
            <RkLogo />
          </NavLink>
        </div>

        <div className="login-form">
          <h1 className="login-title">AlpenWegs</h1>
          <input
            className="login-input"
            type="email"
            placeholder="Email"
            value={email}
            required
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            className="login-input"
            type="password"
            placeholder="Password"
            value={password}
            required
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <div className="login-process">
          {error && <p>{error}</p>}
          <button className="login-button" type="submit" disabled={loading}>
            {loading ? "Logging in…" : "Log in"}
          </button>
        </div>
      </div>
    </form>
  );
}
