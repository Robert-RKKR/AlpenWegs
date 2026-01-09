// React imports:
import ReactDOM from "react-dom/client";
import { App } from "./app/App";
import React from "react";

// Mantine styles:
import "@mantine/core/styles.css";
import '@mantine/dates/styles.css';
import '@mantine/charts/styles.css';

// MapLibre GL CSS import:
// import "maplibre-gl/dist/maplibre-gl.css";

// Main render function:
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
