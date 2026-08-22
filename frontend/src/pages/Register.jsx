import { useState } from "react";
import { registerUser } from "../services/authService";
import { Link } from "react-router-dom";

function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const result = await registerUser({
        username,
        email,
        password,
      });

      alert(result.message);
    } catch (error) {
      alert(
        error.response?.data?.detail ||
        "Registration failed"
      );
    }
  };

  return (
    <div>
      <h1>MailBrain Register</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) =>
            setUsername(e.target.value)
          }
        />

        <br /><br />

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
          Register
        </button>
      </form>

      <br />

      <Link to="/">
        Already have an account?
      </Link>
    </div>
  );
}

export default Register;