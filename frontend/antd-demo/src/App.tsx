// src/App.tsx
import React, { useState } from "react";
import { Form, Input, Button, Card, Typography, message } from "antd";
import axios from "axios";

const { Title } = Typography;

interface User {
  pk: string;
  email: string;
  first_name: string;
  last_name: string;
}

function App() {
  const [loading, setLoading] = useState(false);
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem("access") || null);

  const onFinish = async (values: any) => {
    setLoading(true);
    try {
      const response = await axios.post("http://5.180.148.151:8000/api/auth/login/", {
        email: values.email,
        password: values.password,
      });

      const { access, refresh, user } = response.data.page_results;

      // store tokens
      localStorage.setItem("access", access);
      localStorage.setItem("refresh", refresh);

      setToken(access);
      setUser(user);

      message.success("Login successful!");
    } catch (error: any) {
      console.error(error);
      message.error("Login failed. Please check your credentials.");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    setUser(null);
    setToken(null);
  };

  return (
    <div style={{ display: "flex", justifyContent: "center", marginTop: 100 }}>
      <Card style={{ width: 400 }}>
        {!token ? (
          <>
            <Title level={3} style={{ textAlign: "center" }}>Login</Title>
            <Form
              name="login"
              layout="vertical"
              onFinish={onFinish}
            >
              <Form.Item
                name="email"
                label="Email"
                rules={[{ required: true, message: "Please input your email!" }]}
              >
                <Input placeholder="Enter your email" />
              </Form.Item>

              <Form.Item
                name="password"
                label="Password"
                rules={[{ required: true, message: "Please input your password!" }]}
              >
                <Input.Password placeholder="Enter your password" />
              </Form.Item>

              <Form.Item>
                <Button type="primary" htmlType="submit" block loading={loading}>
                  Login
                </Button>
              </Form.Item>
            </Form>
          </>
        ) : (
          <>
            <Title level={4}>Welcome, {user?.first_name} {user?.last_name}</Title>
            <p><b>Email:</b> {user?.email}</p>
            <p><b>User ID:</b> {user?.pk}</p>

            <Button type="default" danger block onClick={handleLogout}>
              Logout
            </Button>
          </>
        )}
      </Card>
    </div>
  );
}

export default App;
