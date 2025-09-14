import React from "react";
import { Layout } from "antd";

const { Footer } = Layout;

export default function PageFooterComponent() {
  return (
    <Footer style={{ textAlign: "center" }}>
      © {new Date().getFullYear()} AlpenWegs
    </Footer>
  );
}
