import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "../api/axios";

function EmailDetails() {
  const { id } = useParams();

  const navigate = useNavigate();

  const [email, setEmail] = useState(null);

  useEffect(() => {
    loadEmail();
  }, []);

  const loadEmail = async () => {
    try {
      const token =
        localStorage.getItem("token");

      const response =
        await axios.get(
          `/emails/${id}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

      setEmail(response.data.email);
    } catch (error) {
      console.error(error);
      alert("Failed to load email");
    }
  };

  if (!email) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Email Details</h1>

      <button
        onClick={() =>
          navigate("/dashboard")
        }
      >
        Back to Dashboard
      </button>

      <hr />

      <p>
        <strong>ID:</strong>{" "}
        {email.id}
      </p>

      <p>
        <strong>Sender:</strong>{" "}
        {email.sender}
      </p>

      <p>
        <strong>Recipient:</strong>{" "}
        {email.recipient}
      </p>

      <p>
        <strong>Subject:</strong>{" "}
        {email.subject}
      </p>

      <p>
        <strong>Body:</strong>
      </p>

      <div
        style={{
          border: "1px solid gray",
          padding: "10px",
          marginBottom: "15px",
        }}
      >
        {email.body}
      </div>

      <p>
        <strong>Priority:</strong>{" "}
        {email.priority}
      </p>

      <p>
        <strong>Category:</strong>{" "}
        {email.category}
      </p>

      <p>
        <strong>Read:</strong>{" "}
        {email.is_read
          ? "Yes"
          : "No"}
      </p>

      <p>
        <strong>Important:</strong>{" "}
        {email.is_important
          ? "Yes"
          : "No"}
      </p>

      <p>
        <strong>Requires Action:</strong>{" "}
        {email.requires_action
          ? "Yes"
          : "No"}
      </p>
    </div>
  );
}

export default EmailDetails;