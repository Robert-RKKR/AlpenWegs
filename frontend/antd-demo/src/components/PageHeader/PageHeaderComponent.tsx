import React from "react";
import { Layout, Menu } from "antd";
import { Link } from "react-router-dom";

const { Header } = Layout;

export default function PageHeaderComponent() {
  const items = [
    { key: "main", label: <Link to="/">Home</Link> },
    { key: "hiking", label: <Link to="/hiking">Hiking</Link> },
    { key: "login", label: <Link to="/login">Login</Link> },
  ];

  return (
    <Header>
      <div style={{ float: "left", color: "#fff", marginRight: 20 }}>
        🏔 AlpenWegs
      </div>
      <Menu theme="dark" mode="horizontal" items={items} />
    </Header>
  );
}
