import axios from "../api/axios";

export const getEmails = async () => {
  const token = localStorage.getItem("token");

  const response = await axios.get("/emails", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};

export const getStatistics = async () => {
  const token = localStorage.getItem("token");

  const response = await axios.get("/emails/statistics", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};

export const createEmail = async (emailData) => {
  const token = localStorage.getItem("token");

  const response = await axios.post(
    "/emails",
    emailData,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};

export const deleteEmail = async (emailId) => {
  const token = localStorage.getItem("token");

  const response = await axios.delete(
    `/emails/${emailId}`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};

export const markEmailRead = async (
  emailId,
  isRead
) => {
  const token = localStorage.getItem("token");

  const response = await axios.patch(
    `/emails/${emailId}/read?is_read=${isRead}`,
    {},
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};

export const markEmailImportant = async (
  emailId,
  isImportant
) => {
  const token = localStorage.getItem("token");

  const response = await axios.patch(
    `/emails/${emailId}/important?is_important=${isImportant}`,
    {},
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};