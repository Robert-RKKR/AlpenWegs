# To-Do Plan for Your App

## 1. API Test

- [ ] Create a **test endpoint** (`/api/test/`) to verify the API is working.  
- [ ] Return a simple JSON response `{ "status": "ok", "message": "API is working" }`.  
- [ ] Add automated tests (pytest/Django TestCase/FastAPI test client).  

## 2. API for User (User Details)

- [ ] Create `/api/users/` endpoint to manage user data.  
- [ ] Endpoints:
  - `GET /api/users/` → list all users (admin only).
  - `GET /api/users/<id>/` → user details.
  - `POST /api/users/` → register new user.
  - `PUT/PATCH /api/users/<id>/` → update profile.
  - `DELETE /api/users/<id>/` → delete account.  
- [ ] Fields: username, email, first_name, last_name, date_of_birth, height, weight, achievements, etc.  

## 3. Where to Use API

- [ ] **Frontend** → React/Next.js/Vite client requests.  
- [ ] **Mobile App** → iOS/Android integration (later).  
- [ ] **External services** → limited public API (only safe data).  

## 4. User Calculations (BMI)

- [ ] Store `height` (cm) and `weight` (kg) in user profile.  
- [ ] Add endpoint `/api/users/<id>/bmi/` → calculate BMI dynamically:
  - Formula: `BMI = weight / (height/100)^2`.  
  - Response: `{ "bmi": 24.5, "category": "Normal" }`.  
- [ ] Optional: store historical BMI values for statistics.  

## 5. Statistics & Auto-Increment

- [ ] Create `UserStatistic` model linked to `User`.  
- [ ] Track values like:
  - `total_logins`
  - `total_routes`
  - `total_likes`
- [ ] Auto-increment counters whenever an event happens.  
- [ ] Provide `/api/users/<id>/stats/` endpoint for quick overview.  

## 6. Liked Mechanism

- [ ] Implement generic `Like` model:
  - Fields: `user`, `content_type`, `object_id`, `created_at`.  
  - Works for articles, routes, events, etc.  
- [ ] Endpoints:
  - `POST /api/like/` → add like.  
  - `DELETE /api/like/` → remove like.  
  - `GET /api/like/<object_id>/` → check who liked an item.  

## 7. GPX Calculation

- [ ] Create GPX upload endpoint `/api/gpx/upload/`.  
- [ ] Parse GPX with `gpxpy`:
  - Extract distance, elevation gain/loss, min/max elevation.  
  - Calculate average speed (if timestamps available).  
  - Calculate ascent speed.  
- [ ] Return JSON with route summary:

  ```json
  {
    "distance_km": 12.4,
    "elevation_gain": 860,
    "elevation_loss": 840,
    "avg_speed_kmh": 4.3,
    "max_elevation": 2150,
    "min_elevation": 1350
  }
