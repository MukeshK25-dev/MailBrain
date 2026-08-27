import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getEmails,
  getStatistics,
  createEmail,
  deleteEmail,
  markEmailRead,
  markEmailImportant,
} from "../services/emailService";

function Dashboard() {
  const [emails, setEmails] = useState([]);
  const [stats, setStats] = useState(null);

  const [search, setSearch] = useState("");
  const [priority, setPriority] = useState("");
  const [category, setCategory] = useState("");
  const [isRead, setIsRead] = useState("");
  const [isImportant, setIsImportant] = useState("");

  const [sender, setSender] = useState("");
  const [recipient, setRecipient] = useState("");
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");

  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/");
      return;
    }

    loadDashboardData();
  }, []);

  const loadDashboardData = async (
    filters = {}
  ) => {
    try {
      const emailData =
        await getEmails(filters);

      const statsData =
        await getStatistics();

      setEmails(emailData.emails || []);
      setStats(statsData.statistics);
    } catch (error) {
      console.error(error);
      alert("Failed to load dashboard");
    }
  };

  const handleSearch = async () => {
    await loadDashboardData({
      search,
      priority,
      category,
      is_read: isRead,
      is_important: isImportant,
    });
  };

  const handleClearFilters =
    async () => {
      setSearch("");
      setPriority("");
      setCategory("");
      setIsRead("");
      setIsImportant("");

      await loadDashboardData();
    };

  const handleCreateEmail = async (e) => {
    e.preventDefault();

    try {
      await createEmail({
        sender,
        recipient,
        subject,
        body,
      });

      alert(
        "Email created successfully"
      );

      setSender("");
      setRecipient("");
      setSubject("");
      setBody("");

      await handleSearch();
    } catch (error) {
      console.error(error);
      alert("Failed to create email");
    }
  };

  const handleDeleteEmail = async (
    emailId
  ) => {
    try {
      await deleteEmail(emailId);

      alert(
        "Email deleted successfully"
      );

      await handleSearch();
    } catch (error) {
      console.error(error);
      alert("Failed to delete email");
    }
  };

  const handleMarkRead = async (
    emailId,
    currentStatus
  ) => {
    try {
      await markEmailRead(
        emailId,
        !currentStatus
      );

      await handleSearch();
    } catch (error) {
      console.error(error);
      alert(
        "Failed to update read status"
      );
    }
  };

  const handleMarkImportant =
    async (
      emailId,
      currentStatus
    ) => {
      try {
        await markEmailImportant(
          emailId,
          !currentStatus
        );

        await handleSearch();
      } catch (error) {
        console.error(error);
        alert(
          "Failed to update importance"
        );
      }
    };

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

    return (
    <div style={{ padding: "20px" }}>
      <h1>MailBrain Dashboard</h1>

      <button onClick={handleLogout}>
        Logout
      </button>

      <hr />

      <h2>Email Filters</h2>

      <input
        type="text"
        placeholder="Search emails"
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      <br />
      <br />

      <select
        value={priority}
        onChange={(e) =>
          setPriority(e.target.value)
        }
      >
        <option value="">
          All Priorities
        </option>
        <option value="high">
          High
        </option>
        <option value="medium">
          Medium
        </option>
        <option value="low">
          Low
        </option>
      </select>

      {" "}

      <select
        value={category}
        onChange={(e) =>
          setCategory(e.target.value)
        }
      >
        <option value="">
          All Categories
        </option>
        <option value="work">
          Work
        </option>
        <option value="finance">
          Finance
        </option>
        <option value="shopping">
          Shopping
        </option>
        <option value="personal">
          Personal
        </option>
      </select>

      {" "}

      <select
        value={isRead}
        onChange={(e) =>
          setIsRead(e.target.value)
        }
      >
        <option value="">
          All Read Status
        </option>
        <option value="true">
          Read
        </option>
        <option value="false">
          Unread
        </option>
      </select>

      {" "}

      <select
        value={isImportant}
        onChange={(e) =>
          setIsImportant(
            e.target.value
          )
        }
      >
        <option value="">
          All Importance
        </option>
        <option value="true">
          Important
        </option>
        <option value="false">
          Not Important
        </option>
      </select>

      {" "}

      <button onClick={handleSearch}>
        Apply Filters
      </button>

      {" "}

      <button
        onClick={handleClearFilters}
      >
        Clear Filters
      </button>

      <hr />

      <h2>Create Email</h2>

      <form onSubmit={handleCreateEmail}>
        <input
          type="text"
          placeholder="Sender"
          value={sender}
          onChange={(e) =>
            setSender(e.target.value)
          }
          required
        />

        <br />
        <br />

        <input
          type="text"
          placeholder="Recipient"
          value={recipient}
          onChange={(e) =>
            setRecipient(
              e.target.value
            )
          }
          required
        />

        <br />
        <br />

        <input
          type="text"
          placeholder="Subject"
          value={subject}
          onChange={(e) =>
            setSubject(e.target.value)
          }
          required
        />

        <br />
        <br />

        <textarea
          placeholder="Email Body"
          value={body}
          onChange={(e) =>
            setBody(e.target.value)
          }
          rows="5"
          cols="50"
          required
        />

        <br />
        <br />

        <button type="submit">
          Create Email
        </button>
      </form>

      <hr />

      <h2>Statistics</h2>

      {stats ? (
        <div>
          <p>Total Emails: {stats.total_emails}</p>
          <p>Read Emails: {stats.read_emails}</p>
          <p>Unread Emails: {stats.unread_emails}</p>
          <p>Important Emails: {stats.important_emails}</p>
          <p>
            Action Required:{" "}
            {stats.action_required_emails}
          </p>
          <p>High Priority: {stats.high_priority}</p>
          <p>
            Medium Priority: {stats.medium_priority}
          </p>
          <p>Low Priority: {stats.low_priority}</p>
        </div>
      ) : (
        <p>Loading statistics...</p>
      )}

      <hr />

            <h2>Email List</h2>

      {emails.length === 0 ? (
        <p>No emails found.</p>
      ) : (
        <table
          border="1"
          cellPadding="10"
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Subject</th>
              <th>Sender</th>
              <th>Priority</th>
              <th>Category</th>
              <th>Read</th>
              <th>Important</th>
              <th>Action Required</th>
              <th>View</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {emails.map((email) => (
              <tr key={email.id}>
                <td>{email.id}</td>
                <td>{email.subject}</td>
                <td>{email.sender}</td>
                <td>{email.priority}</td>
                <td>{email.category}</td>

                <td>
                  {email.is_read
                    ? "Yes"
                    : "No"}
                </td>

                <td>
                  {email.is_important
                    ? "Yes"
                    : "No"}
                </td>

                <td>
                  {email.requires_action
                    ? "Yes"
                    : "No"}
                </td>

                <td>
                  <button
                    onClick={() =>
                      navigate(
                        `/emails/${email.id}`
                      )
                    }
                  >
                    View
                  </button>
                </td>

                <td>
                  <button
                    onClick={() =>
                      handleMarkRead(
                        email.id,
                        email.is_read
                      )
                    }
                  >
                    {email.is_read
                      ? "Unread"
                      : "Read"}
                  </button>

                  {" "}

                  <button
                    onClick={() =>
                      handleMarkImportant(
                        email.id,
                        email.is_important
                      )
                    }
                  >
                    {email.is_important
                      ? "Unimportant"
                      : "Important"}
                  </button>

                  {" "}

                  <button
                    onClick={() =>
                      handleDeleteEmail(
                        email.id
                      )
                    }
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Dashboard;