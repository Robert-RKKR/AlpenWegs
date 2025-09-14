import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import 'antd/dist/reset.css';
// Application CSS imports:
import './styles/reset.css';
import './styles/main.css';

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
