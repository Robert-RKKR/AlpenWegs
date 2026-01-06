// Import application components:
import { useAuthStore } from "../../../../stores/authStore";
import { RkLogo } from "../../../../assets/logo/RkLogo";
import { login } from "../../api/authApi";

// Import React components:
import { useNavigate } from "react-router-dom";
import { NavLink } from "react-router-dom";import { useState } from "react";
import axios from "axios";

// Import component css:
import "./LoginPage.css";

// LoginPage component:
export function LoginPage() {
  const navigate = useNavigate();

  // Zustand action:
  const setAuth = useAuthStore((s) => s.setAuth);

  // Form state:
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);

  // UI state:
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

      // Persist auth + remember-me flag:
      setAuth(user, access, refresh, rememberMe);

      navigate("/auth/profile");
    } catch (err) {
      if (axios.isAxiosError(err)) {
        setError(
          err.response?.data?.page_error?.error_message ??
            "Invalid email or password"
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
        {/* Logo */}
        <div className="login-logo">
          <NavLink to="/" aria-label="AlpenWegs Homepage">
            <RkLogo />
          </NavLink>
        </div>

        {/* Form */}
        <div className="login-form">
          <h1 className="login-title">AlpenWegs</h1>

          <input
            className="login-input"
            type="email"
            placeholder="Email"
            value={email}
            required
            autoComplete="email"
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            className="login-input"
            type="password"
            placeholder="Password"
            value={password}
            required
            autoComplete="current-password"
            onChange={(e) => setPassword(e.target.value)}
          />

          {/* Remember me */}
          <label className="login-remember">
            <input
              type="checkbox"
              checked={rememberMe}
              onChange={(e) => setRememberMe(e.target.checked)}
            />
            Keep me logged in
          </label>
        </div>

        {/* Actions */}
        <div className="login-process">
          {error && <p className="login-error">{error}</p>}

          <button
            className="login-button"
            type="submit"
            disabled={loading}
          >
            {loading ? "Logging in…" : "Log in"}
          </button>
        </div>
      </div>
    </form>
  );
}
