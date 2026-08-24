import axios from "../api/axios";

const getAuthHeaders = () => {
  const token = localStorage.getItem("token");

  return {
    Authorization: `Bearer ${token}`,
  };
};

export const getEmails = async (filters = {}) => {
  const params = new URLSearchParams();

  if (filters.search) {
    params.append("search", filters.search);
  }

  if (filters.priority) {
    params.append("priority", filters.priority);
  }

  if (filters.category) {
    params.append("category", filters.category);
  }

  if (
    filters.is_read !== undefined &&
    filters.is_read !== ""
  ) {
    params.append("is_read", filters.is_read);
  }

  if (
    filters.is_important !== undefined &&
    filters.is_important !== ""
  ) {
    params.append(
      "is_important",
      filters.is_important
    );
  }

  let url = "/emails";

  if (params.toString()) {
    url += `?${params.toString()}`;
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

export const analyzeEmail = async (
  emailData
) => {
  const response = await axios.post(
    "/emails/analyze",
    emailData,
    {
      headers: getAuthHeaders(),
    }
  );

  return response.data;
};
