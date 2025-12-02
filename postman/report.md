Data Engineering Assessment – Project Report
1. Project Overview

This project implements a complete Data Engineering workflow consisting of:

PostgreSQL database schema

FastAPI service with CRUD APIs

ETL pipeline to aggregate user data

Postman collection for API testing

GitHub-ready project structure

Documentation (README.md + report.md)

The solution covers all evaluation requirements.

2. Database Design

Three tables are created:

users

Stores personal details of users.

user_bank_info

Stores user bank information (1-to-1 mapping).

employment_info

Stores user employment details including salary.

All tables use proper Primary & Foreign Keys to ensure data integrity.

3. FastAPI Service

The API includes full CRUD operations:

Create User

List Users

Get User by ID

Update User

Delete User

Additional modules implemented:

models.py — SQLAlchemy ORM models

schemas.py — Pydantic schemas

database.py — DB connection

routers/ — User API routes

main.py — Root application setup

The API runs using:

uvicorn service.app.main:app --reload

4. ETL Pipeline

A Python ETL script (etl/group_users.py) performs:

Extract → Read data from PostgreSQL

Transform → Merge tables and aggregate

Load → Save output to CSV (output/grouped_users.csv)

Output format:

city	user_count	total_salary

This validates the ETL pipeline functionality.

5. Postman Collection

A Postman collection is included containing:

Create User (POST)

Get User (GET)

List Users (GET)

Update User (PUT)

Delete User (DELETE)

Each request contains an example payload for easy testing.

6. How to Run the Project
Backend API
cd service/app
uvicorn main:app --reload

ETL
cd etl
python group_users.py

7. GitHub Project Structure
Data_Engineering/
│── service/
│   └── app/
│       ├── main.py
│       ├── models.py
│       ├── schemas.py
│       ├── database.py
│       └── routers/
│           └── users.py
│── etl/
│   └── group_users.py
│── output/
│   └── grouped_users.csv
│── postman_collection.json
│── README.md
└── report.md

8. Conclusion

All requirements from the assessment are completed:

✔ API functionality

✔ Database schema & integrity

✔ ETL workflow

✔ Postman collection

✔ Documentation

✔ Ready for GitHub submission

This project demonstrates the understanding of backend API design, SQL modeling, and ETL pipelines expected from a Data Engineering role.