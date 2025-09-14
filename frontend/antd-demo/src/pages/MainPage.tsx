import React from "react";
import { Typography } from "antd";

const { Title } = Typography;

export default function MainPage() {
  const user = localStorage.getItem("user");
  const parsed = user ? JSON.parse(user) : null;

  return (
    <div style={{ textAlign: "center", marginTop: 50 }}>
      <Title level={2}>Welcome to AlpenWegs</Title>
      {parsed ? (
        <p>
          Logged in as <b>{parsed.first_name} {parsed.last_name}</b> ({parsed.email})
        </p>
      ) : (
        <p>Please log in to access more features.</p>
      )}
    </div>
  );
}
