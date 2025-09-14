import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import { Layout } from "antd";

import PageHeaderComponent from './components/PageHeader/PageHeaderComponent'
import PageFooterComponent from './components/PageFooter/PageFooterComponent'
import AppRouter from "./router";

const { Content } = Layout;

function App() {
  return (
    <Router>
      <Layout style={{ minHeight: "100vh" }}>
        <PageHeaderComponent />
        <Content style={{ padding: "20px 50px", flex: 1 }}>
          <AppRouter />
        </Content>
        <PageFooterComponent />
      </Layout>
    </Router>
  );
}

export default App;
