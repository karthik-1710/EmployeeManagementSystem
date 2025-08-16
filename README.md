# Hafta - HR Management System

## Overview
Hafta is a comprehensive Human Resource Management System built with Python Flask for managing employee data, attendance, payroll, and performance tracking.

## Features
- Employee management
- Attendance tracking
- Payroll processing
- Performance evaluation
- Master data management
- Reporting and analytics
- Multi-company support

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize database: `flask db upgrade`
4. Run: `python run.py`

## Usage
Access the application at `http://localhost:5000` after starting the server.

## Project Structure
- `app/` - Main application code
- `migrations/` - Database migrations
- `docs/` - Documentation
- `requirements.txt` - Python dependencies

## Configuration
Set environment variables in `.env` file:
- FLASK_APP=run.py
- FLASK_ENV=development
- SECRET_KEY=your-secret-key

