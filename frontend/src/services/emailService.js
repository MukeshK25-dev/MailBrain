import axios from "../api/axios";

const getAuthHeaders = () => {
  const token = localStorage.getItem("token");

  return {
    Authorization: `Bearer ${token}`,
  };
};

export const getEmails = async (search = "") => {
  let url = "/emails";

  if (search.trim()) {
    url += `?search=${encodeURIComponent(search)}`;
  }

  const response = await axios.get(url, {
    headers: getAuthHeaders(),
  });

  return response.data;
};

export const getStatistics = async () => {
  const response = await axios.get(
    "/emails/statistics",
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};

export const createEmail = async (emailData) => {
  const response = await axios.post(
    "/emails",
    emailData,
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};

export const deleteEmail = async (emailId) => {
  const response = await axios.delete(
    `/emails/${emailId}`,
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};

export const markEmailRead = async (
  emailId,
  isRead
) => {
  const response = await axios.patch(
    `/emails/${emailId}/read?is_read=${isRead}`,
    {},
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};

export const markEmailImportant = async (
  emailId,
  isImportant
) => {
  const response = await axios.patch(
    `/emails/${emailId}/important?is_important=${isImportant}`,
    {},
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};