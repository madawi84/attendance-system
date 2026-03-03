# Attendance System (حاظر)

A **geolocation-based attendance system** designed for organisations to manage employee check-in and check-out using **location validation, role-based access control (RBAC), and a scalable REST API backend**.

This project is built with **Django** and **Django REST Framework** and is designed to support both **web admin panels and mobile applications**.

Repository:  
https://github.com/madawi84/attendance-system

---

# Work in Progress

This project is currently under active development.

One of the planned improvements is enhancing the **location visualization experience**. The current implementation validates employee attendance using **latitude, longitude, and radius-based geofencing**.

Future versions will introduce a **map-based geolocation interface**, allowing users to visually interact with attendance zones directly on a map.

The goal is to implement a **real-time geospatial visualization layer** where the permitted attendance area is displayed as an interactive overlay (geofence) on a digital map. This will provide a more intuitive user experience similar to modern location-based applications.

Planned technologies and concepts include:

- Interactive map integration (e.g., Mapbox, Leaflet, or Google Maps API)
- Real-time GPS positioning
- Geofence visualization using circular or polygon overlays
- Dynamic radius validation
- Improved user feedback when entering or leaving an authorised attendance zone

These enhancements aim to improve **usability, transparency, and accuracy** in location-based attendance verification.

---

# Features

- Company-based structure (users belong to a company)
- Location-based attendance (latitude, longitude, radius)
- Check-in / Check-out attendance records
- Role-Based Access Control (HR, managers, supervisors)
- REST API for integration with mobile apps
- Django Admin panel for management
- Scalable architecture for enterprise use

Future planned features:

- Offline attendance mode with sync
- Biometric authentication
- Email notifications
- Integration with Oracle Fusion HR
- Reporting and analytics dashboard

---

# Technology Stack

Backend
- Python
- Django
- Django REST Framework

Database
- PostgreSQL (recommended)
- SQLite (for development)

Authentication
- Django authentication system
- Extendable to JWT

Resources:

Django  
https://www.djangoproject.com/

Django REST Framework  
https://www.django-rest-framework.org/

PostgreSQL  
https://www.postgresql.org/

---

# Project Structure

Example structure of the project:

```
attendance-system
│
├── attendance/        # Attendance logic
├── companies/         # Company models
├── locations/         # Geofenced locations
├── users/             # User roles and permissions
├── manage.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1 Clone the repository

```bash
git clone https://github.com/madawi84/attendance-system.git
cd attendance-system
```

---

## 2 Create a virtual environment

Windows

```powershell
python -m venv env
env\Scripts\activate
```

Mac / Linux

```bash
python3 -m venv env
source env/bin/activate
```

Python virtual environments  
https://docs.python.org/3/library/venv.html

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5 Create admin user

```bash
python manage.py createsuperuser
```

---

## 6 Run the server

```bash
python manage.py runserver
```

Open:

Admin panel

```
http://127.0.0.1:8000/admin
```

API root

```
http://127.0.0.1:8000/api
```

---

# Example API Endpoints

Authentication

```
POST /api/login
```

Locations

```
GET /api/locations
POST /api/locations
```

Attendance

```
POST /api/check-in
POST /api/check-out
GET  /api/attendance-records
```

---

# Example Location Object

```
{
  "company": 1,
  "name": "Main Office",
  "latitude": 24.7136,
  "longitude": 46.6753,
  "radius": 150
}
```

---

# Development

Recommended tools

- Visual Studio Code
- Python extension
- REST Client

VS Code Python guide  
https://code.visualstudio.com/docs/python/python-tutorial

Django tutorial  
https://docs.djangoproject.com/en/stable/intro/tutorial01/

---

# Roadmap

Future improvements planned for the system:

- Mobile app for employees
- Biometric attendance
- Offline attendance mode
- Email notifications
- Advanced reporting dashboard
- Oracle Fusion HR integration
- Custom role management

---

# Contributing

Contributions are welcome.

Steps:

1 Fork the repository  
2 Create a feature branch  
3 Commit your changes  
4 Open a Pull Request  

GitHub pull request guide  
https://docs.github.com/en/pull-requests

---

# Author

Madawi Faisal Al Soyohi

GitHub  
https://github.com/madawi84
