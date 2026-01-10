// Imports:
import { 
  IconRoute, IconNavigation, IconPhoto, IconBook2,
  IconUsersGroup, IconCookie, IconGauge, IconUser,
  IconMountain, IconTimeline, IconMap2
} from '@tabler/icons-react';

/* Primary feature navigation (top section) */
export const primaryFeatures = [
  {
    icon: IconRoute,
    title: "Plan your adventure",
    description:
      "Create single-day or multi-day hiking, biking, or trail running plans with flexible routes, difficulty options, and terrain-aware paths across Switzerland.",
    to: "/explorer",
  },
  {
    icon: IconNavigation,
    title: "Navigate and track",
    description:
      "Follow your planned trail in real time with geolocation tracking, checkpoints, and route guidance while recording your activity on the go.",
    to: "/explorer/track",
  },
  {
    icon: IconPhoto,
    title: "Record and relive",
    description:
      "Save completed activities with GPX tracks, photos, notes, and personal tags to build a meaningful adventure journal and lasting memories.",
    to: "/profiles/journal",
  },
  {
    icon: IconBook2,
    title: "Explore the Compendium",
    description:
      "Discover in-depth knowledge about Swiss regions, trails, landmarks, and nature to deepen your connection with every place you visit.",
    to: "/compendium",
  },
  {
    icon: IconUsersGroup,
    title: "Hike together",
    description:
      "Create or join outdoor events, meet fellow enthusiasts, and explore trails together through community-driven hikes.",
    to: "/events",
  },
];

/* Platform principles / values (secondary section) */
export const platformHighlights = [
  {
    title: "Performance-focused",
    description:
      "Optimized route processing, GPX handling, and statistics ensure fast interaction even with complex multi-day adventures.",
    icon: IconGauge,
    to: "/about/performance",
  },
  {
    title: "Privacy by design",
    description:
      "Your activities, routes, and memories remain under your control, with transparent data handling and no hidden tracking.",
    icon: IconUser,
    to: "/about/privacy",
  },
  {
    title: "No third-party dependency lock-in",
    description:
      "AlpenWeg avoids unnecessary external platforms, keeping your data portable and the system future-proof.",
    icon: IconCookie,
    to: "/about/architecture",
  },
  {
    title: "Built for the Alps",
    description:
      "Designed specifically for alpine terrain, Swiss regions, elevation profiles, and real-world hiking conditions.",
    icon: IconMountain,
    to: "/about/alpine-focus",
  },
  {
    title: "Your journey over time",
    description:
      "Track seasonal goals, milestones, and long-term progress across years, not just individual trips.",
    icon: IconTimeline,
    to: "/about/goals",
  },
  {
    title: "Geography-first design",
    description:
      "Maps, regions, routes, and points of interest are first-class elements throughout the entire platform.",
    icon: IconMap2,
    to: "/about/geography",
  },
];
