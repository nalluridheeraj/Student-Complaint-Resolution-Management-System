# Student Complaint & Resolution Management System

## Overview
A backend-focused web application built using Django to manage student complaints with role-based access control. Students can submit and track complaints, while administrators can view all complaints and update their status.

## Features
- User authentication using Django auth
- Role-based access (Student / Admin)
- Students can submit and view their own complaints
- Admins can view all complaints and update status
- Complaint categorization and status tracking

## Tech Stack
- Backend: Python, Django
- Database: SQLite (can be switched to MySQL)
- Frontend: HTML (Django Templates)
- Tools: Git, GitHub

## Data Models
- User (Django default)
- Profile (OneToOne with User, stores role)
- Complaint (category, status, created_by, timestamps)

## How to Run
```bash
git clone <repo-url>
cd Student-Complaint-Resolution-Management-System
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
