import { useState } from "react";
import { loginUser } from "../services/authService";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const result = await loginUser({
        email,
        password,
      });

      localStorage.setItem(
        "token",
        result.access_token
      );

      alert("Login successful");

      navigate("/dashboard");
    } catch (error) {
      alert(
        error.response?.data?.detail ||
        "Login failed"
      );
    }
  };

  return (
    <div>
      <h1>MailBrain Login</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <br /><br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <br /><br />

        <button type="submit">
          Login
        </button>
      </form>

      <br />

      <Link to="/register">
        Create Account
      </Link>
    </div>
  );
}

export default Login;