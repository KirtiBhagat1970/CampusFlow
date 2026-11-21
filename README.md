
# CampusFlow: Smart Student Productivity & Academic Planning Web Application

> One place for a student's tasks, assignments, attendance and exam preparation.

**Capstone Team Project | FY MCA (2026-2028) | Division A | Group 18**
Maharashtra Education Society's Institute of Management and Career Courses (IMCC), Pune (Autonomous)

---

## Table of Contents

1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Objectives](#objectives)
4. [Features / Modules](#features--modules)
5. [Recommendation Engine Logic](#recommendation-engine-logic)
6. [Tech Stack](#tech-stack)
7. [Project Structure](#project-structure)
8. [Getting Started](#getting-started)
9. [Usage](#usage)
10. [Expected Output](#expected-output)
11. [Project Team](#project-team)
12. [Acknowledgements](#acknowledgements)

---

## Overview

CampusFlow is a responsive full-stack web application built with Python and Flask. It lets students manage tasks, assignment deadlines, subject-wise attendance and exam preparation from a single dashboard, and works on laptops, tablets and phones. Each student has a private, secure account, so they only ever see their own data.

## Problem Statement

Students usually manage tasks, assignments, attendance and exam preparation with separate tools, notebooks or just memory. This makes it hard to track deadlines and academic progress consistently, and students often find out about low attendance or poor exam preparation too late.

CampusFlow solves this with a single, easy-to-use and responsive application that combines all of these activities and presents useful academic information in one place.

## Objectives

1. Provide one centralized platform for academic planning.
2. Let students manage tasks with priority and deadline.
3. Track assignment deadlines and submission status.
4. Calculate subject-wise attendance percentage automatically against the 75% target.
5. Track exam dates and preparation level.
6. Show academic progress through visual charts.
7. Give rule-based study recommendations on what to do next.
8. Keep each student's data private through secure login.

## Features / Modules

| # | Module | Description |
|---|--------|-------------|
| M1 | **User Authentication & Role Management** | Student registration, login and logout. Passwords are stored as hashes. Every page except landing, login and register is protected, so each student sees only their own records. |
| M2 | **Dashboard** | One-screen summary: task statistics, average attendance, number of upcoming exams, upcoming assignments, the daily recommendation and charts. |
| M3 | **Task Manager** | Add tasks with title, category, priority (High / Medium / Low) and deadline. Mark tasks complete or pending, and delete them. |
| M4 | **Assignment Tracker** | Record assignments with subject and due date. Mark them submitted or pending, or delete them. |
| M5 | **Attendance Calculator** | Store classes held and classes attended per subject. The attendance percentage is calculated automatically against a 75% target. |
| M6 | **Exam Planner** | Store exam dates and preparation percentage for each exam, and see the number of days remaining. |
| M7 | **Analytics** | Doughnut chart of task status and bar chart of subject-wise attendance, built with Chart.js. |
| M8 | **Recommendation Engine** | Rule-based suggestion of what to do next (see below). |

## Recommendation Engine Logic

The engine checks the following rules **in order** and shows the first one that applies:

1. The oldest overdue task
2. The nearest exam with preparation below 60%
3. Any subject with attendance below 75%
4. The highest-priority pending task

## Tech Stack

**Backend**
- Python 3
- Flask
- Flask-SQLAlchemy (SQLAlchemy ORM)
- Flask-Login (session management)
- Werkzeug (password hashing)

**Frontend**
- HTML5
- CSS3
- JavaScript
- Jinja2 (templating)
- Chart.js (charts)

**Database**
- SQLite

## Project Structure

A suggested layout (adjust to match your actual code):

```
campusflow/
├── app.py                 # Flask app, routes and configuration
├── models.py              # SQLAlchemy models (User, Task, Assignment, Subject, Exam)
├── requirements.txt       # Python dependencies
├── instance/
│   └── campusflow.db      # SQLite database (created automatically)
├── templates/             # Jinja2 HTML templates
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── tasks.html
│   ├── assignments.html
│   ├── attendance.html
│   └── exams.html
└── static/
    ├── css/
    └── js/                # Chart.js setup and page scripts
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone <your-repository-url>
cd campusflow

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install flask flask-sqlalchemy flask-login
# or, if requirements.txt is present:
# pip install -r requirements.txt

# 4. Run the application
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

The SQLite database is created automatically the first time the app runs.

## Usage

1. Open the landing page and **register** a new student account.
2. **Log in** to reach your private dashboard.
3. Add your **tasks** with a category, priority and deadline.
4. Add **assignments** and mark them submitted when done.
5. Enter classes held and attended per subject in the **attendance** page. The app shows your percentage and warns you if it drops below 75%.
6. Add **exams** with their dates and your preparation percentage.
7. Check the **dashboard** and **analytics** charts, and follow the daily recommendation.

## Expected Output

A working, responsive website that students can open on a laptop, tablet or phone. Students can see all deadlines, attendance and exam preparation in one dashboard and are less likely to miss work. Automatic attendance calculation warns them when a subject falls below 75%, charts give a quick view of progress, and the daily recommendation shows what to focus on.

The team also gains practical experience in Python, Flask, databases, authentication and responsive web design.

## Project Team

| # | Name | Roll No. | Role |
|---|------|----------|------|
| 1 | Kirti Bhagat | 2601014 | Team Leader |
| 2 | Janhavi Karadkhedkar | 2601096 | Core Team Member |

## Acknowledgements

- **Internal Faculty Guide:** Dr. Kalpana Sudam Dhende
- **External Industry Guide:** Aditya Kulkarni
- Department of Computer Applications (MCA), MES IMCC, Pune
