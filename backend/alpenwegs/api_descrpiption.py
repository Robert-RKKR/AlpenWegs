API_DESCRIPTION = """
The **AlpenWegs REST API** provides access to all resources of the AlpenWegs 
platform, a system for exploring, documenting, and sharing Swiss outdoor 
adventures such as hiking routes, multi-day trips, cultural points of interest, 
and user achievements.

### Core Features
- **Profiles**: User accounts, settings, and achievements.
- **Explorer**: Management of routes, sections, GPX data, and multi-day trips.
- **Compendium**: Knowledge base with articles, points of interest, cards, and regions.
- **Assets**: File and media handling (photos, GPX uploads).
- **Events**: Community and system-organized outdoor events.
- **Notifications**: System-wide messaging and alerts.

### Authentication
- Supports **JWT (JSON Web Token)** via `dj-rest-auth` and `django-allauth`.
- Endpoints available for registration, login, logout, token refresh, and 
  social authentication (Google OAuth).

### Standards & Conventions
- Follows **RESTful design principles**.
- Utilizes **Django REST Framework (DRF)** serializers, views, and permissions.
- API schema generated via **drf-spectacular**, fully OpenAPI 3.0 compliant.

### Usage Notes
- Authorization headers use the `Bearer <token>` scheme.
- All endpoints return JSON responses with consistent success/error formats.
- Pagination, filtering, and search available where applicable.

---

This API is designed for developers building web, mobile, or data analysis 
tools on top of the AlpenWegs platform.
"""