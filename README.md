# 🌿 FloraSpot - Urban Greenspace & Foraging API

FloraSpot is a Django-based REST API that enables users to discover, submit, and moderate community greenspaces such as public fruit trees, wild edible spots, and community gardens. It is designed to support community mapping and sustainable urban foraging efforts.

---

## 🚀 Features

* **JWT Authentication**: Secure access to protected routes
* **Spot Submission**: Authenticated users can submit new foraging locations
* **Public Discovery**: Anyone can explore approved spots
* **Moderation System**: Admins can approve, reject, or manage submissions
* **Timestamping**: Automatic tracking of created and updated times
* **Categorization**: Classify spots by type (fruit tree, herb garden, etc.)

---

## 📦 Tech Stack

* **Backend**: Django + Django REST Framework
* **Database**: PostgreSQL (with optional PostGIS for geospatial support)
* **Authentication**: JWT via `djangorestframework-simplejwt`

---

## ⚙️ Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourusername/floraspot.git
cd floraspot
```

2. **Create virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Setup PostgreSQL:**

* Create a PostgreSQL database and user
* Enable PostGIS extension (optional but recommended)

5. **Set environment variables:**
   Create a `.env` file from the sample:

```bash
cp .env.sample .env
```

Edit `.env` with your `SECRET_KEY`, database credentials, JWT config, etc.

6. **Run migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Start server:**

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 🧪 API Endpoints Summary

### 🧑‍💼 Auth

| Endpoint              | Method | Description                  |
| --------------------- | ------ | ---------------------------- |
| `/api/auth/register/` | POST   | Register a new user          |
| `/api/auth/login/`    | POST   | Login and receive JWT tokens |

### 📍 Spot Management

| Endpoint                    | Method | Auth | Description        |
| --------------------------- | ------ | ---- | ------------------ |
| `/api/spots/`               | GET    | ❌    | Get approved spots |
| `/api/spots/create/`        | POST   | ✅    | Submit a new spot  |
| `/api/spots/mysubmissions/` | GET    | ✅    | Get all your spots |

### 🔧 Moderation

| Endpoint                         | Method | Auth      | Description            |
| -------------------------------- | ------ | --------- | ---------------------- |
| `/api/spots/moderation/pending/` | GET    | ✅ (Staff) | List all pending spots |
| `/api/spots/<id>/approve/`       | POST   | ✅ (Staff) | Approve a spot         |
| `/api/spots/<id>/reject/`        | POST   | ✅ (Staff) | Reject a spot          |

---

## 🔑 Example JWT Usage

All protected routes require:

```
Authorization: Bearer <access_token>
Content-Type: application/json
```

---

## 🧭 Optional Features (Future Roadmap)

* 🔍 Geospatial filtering with PostGIS
* 📷 Image uploads (instead of URL-only)
* ✅ Community verification system
* 🔔 Email or in-app notifications

---
