# Task Management API

A full-stack AI-powered task management application built with FastAPI, PostgreSQL, React, and OpenAI API.

Built as a production-like backend and AI engineering project with a strong focus on:

* clean architecture
* scalable backend structure
* authentication
* testing
* Docker workflows
* CI/CD
* AI integrations

## Live Demo

Demo login credentials are available on request.

Frontend: https://task-management-api-blush.vercel.app  
API Docs: https://task-management-api-p0b1.onrender.com/docs

Deployment:
- Frontend hosted on Vercel
- Backend API hosted on Render
- PostgreSQL database hosted on Render

> Note: This project uses free-tier hosting. The backend may take a few seconds to wake up after periods of inactivity. In some cases, the service or database may be paused or unavailable due to free-tier limits.

> Public registration is disabled for the live demo to prevent spam and uncontrolled AI API usage. The app cannot be used without demo login credentials, which can be provided on request. The Swagger API documentation is public for inspection, but endpoints require authentication and cannot be executed without valid login credentials.

---

# Features

## Backend

* RESTful API design
* JWT authentication
* Role-based access control
* Full CRUD for tasks
* User self-service endpoints
* Admin user management endpoints
* Filtering, pagination, sorting, and search
* PostgreSQL + SQLAlchemy + Alembic
* Validation with Pydantic
* Tests with pytest
* Ruff linting
* Docker-based setup
* GitHub Actions CI

## Frontend

* React + TypeScript
* React Query
* Feature-based architecture
* Reusable components
* Custom hooks
* Task creation/editing UI
* Filtering and sorting
* AI integration UI

## AI Features

### AI Task Improvement

Improves a task title and description based on the user's input.

Example:
- short input: `fix login`
- improved output: clearer title and more useful description

### AI Task Planning

Generates a practical execution plan for open tasks.

The planning logic considers:

- due dates
- priority
- urgency
- estimated effort
- possible task dependencies

Tasks with deadlines are prioritized by due date. Tasks without due dates are still included and ordered by priority and estimated effort.

### AI Task Grouping

Groups open tasks into practical categories such as:

- Work
- Learning
- Personal
- Health
- Admin

This helps organize larger task lists into more manageable sections.

---

### Screenshots

### Register

![Register](docs/screenshots/03_Registering.png)

### Login

![Login](docs/screenshots/04_Logging_In.png)

### Task Dashboard

![Task Dashboard](docs/screenshots/05_Task_Dashboard.png)

### Edit Task and improve with Ai

![Edit Task](docs/screenshots/13_Result_Improve_Task_With_AI.png)

### Task List

![Task List](docs/screenshots/14_Task_List.png)

## AI Task Plan

![AI Task Plan](docs/screenshots/17_Ai_Plan.png)

## AI Plan and Groups

![AI Plan and Task Groups](docs/screenshots/19_Ai_Plan_and_Groups.png)

Additional screenshots are available in the `docs/screenshots/` directory.

# Tech Stack

## Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* pytest
* Ruff
* Docker

## Frontend

* React
* TypeScript
* Vite
* React Query

## AI

* OpenAI API
* GPT-4o-mini

---

# API Endpoints

## Authentication

* `POST /auth/register`
* `POST /auth/login`

## Users

### Self (Authenticated User)

* `GET /users/me`
* `PUT /users/me`
* `PATCH /users/me`
* `DELETE /users/me`

### Admin Only

* `GET /users`
* `GET /users/{id}`
* `PUT /users/{id}`
* `PATCH /users/{id}`
* `DELETE /users/{id}`

## Tasks

* `POST /tasks`
* `GET /tasks`
* `GET /tasks/{id}`
* `PUT /tasks/{id}`
* `PATCH /tasks/{id}`
* `DELETE /tasks/{id}`

## AI

* `POST /ai/improve-task`
* `POST /ai/tasks/{id}/improve`
* `GET /ai/group-tasks`
* `GET /ai/plan`

---


# Advanced Querying

* Filtering (`completed=true/false`)
* Pagination (`limit`, `offset`)
* Sorting (`sort_by`, `order`)
* Search (`search` in title/description)

---

# Project Structure

```text
project-root/
├── backend/
│   ├── alembic/          # Database migrations
│   ├── app/              # FastAPI application
│   │   ├── api/          # API routes
│   │   ├── core/         # Config, database, security
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   └── services/     # Business logic
│   ├── scripts/          # Utility scripts
│   ├── tests/            # Pytest test suite
│   ├── Dockerfile
│   └── requirements*.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/          # App setup, router, providers
│   │   ├── features/     # Feature modules
│   │   ├── lib/          # API client, env, query client
│   │   └── styles/       # Global styles
│   ├── package.json
│   └── vite.config.ts
│
├── .github/workflows/    # GitHub Actions CI
├── compose.yaml
├── compose.dev.yaml
└── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/rnkraus/task_management_api.git
cd task_management_api
```

### 2. Python Environment (for Tests & Alembic)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r backend/requirements-dev.txt
```

### 3. Create Environment Files

Generate a secure key for JWT authentication:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Create the following four `.env` files and replace the placeholder values with your own:

- choose a secure password for the database
- insert your generated `SECRET_KEY`
- insert your OpenAI API key

#### .env (Docker Compose / PostgreSQL)

```env
POSTGRES_DB=taskdb
POSTGRES_USER=taskuser
POSTGRES_PASSWORD=your_password_here
```

#### backend/.env (FastAPI inside Docker)

```env
DATABASE_URL=postgresql://taskuser:your_password_here@db:5432/taskdb

SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=60

OPENAI_API_KEY=your_openai_key_here
```

#### backend/.env.local (for local tools like Alembic):

```env
DATABASE_URL=postgresql://taskuser:your_password_here@localhost:5432/taskdb

SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=60

OPENAI_API_KEY=your_openai_key_here
```

#### backend/.env.test (for pytest):

```env
DATABASE_URL=postgresql://taskuser:your_password_here@localhost:5432/taskdb_test

SECRET_KEY=your_secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

#### frontend/.env.local (Frontend API URL)

```env
VITE_API_URL=http://localhost:8000
```

### 4. Start Docker (Development Mode)

```bash
docker compose --env-file ./backend/.env -f compose.yaml -f compose.dev.yaml up --build
```

### 5. Run Migrations

In a separate terminal:
```bash
cd backend
alembic upgrade head
```

---

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```
Frontend runs at:

```text
http://localhost:5173
```

Make sure the backend is running at:

```text
http://localhost:8000
```


## API Docs (Swagger)

If you want to inspect or test the backend API directly, open:

http://localhost:8000/docs

Swagger UI provides interactive API documentation.

Steps:
1. Open `POST /auth/register`
2. Click "Try it out"
3. Enter the registration data
4. Click "Execute"
5. Click "Authorize" in the top right corner
6. Enter your email in the `username` field
7. Enter your password
8. Click "Authorize"
9. Use protected endpoints such as `/tasks` or `/users/me`

After authorization, Swagger UI automatically includes the access token in protected requests.

## Admin

Promote a user to admin:
```bash
cd backend
python -m scripts.make_admin user@example.com
```

---

## Tests

```bash
cd backend
pytest -v
```

---

## Linting

```bash
cd backend
ruff check .
```


## Database

- PostgreSQL via Docker
- Migrations with Alembic
- Separate test database (taskdb_test)
- Test DB is automatically created during container initialization

---

## Behavior

- Users can only access their own tasks
- Admins can manage all users
- Users cannot be deleted if tasks exist
- Duplicate email addresses are prevented
- Task titles cannot be empty
- PATCH requests must include at least one field
- PUT replaces an object completely, PATCH performs a partial update

---

## Docker

### Standard:

```bash
docker compose --env-file ./backend/.env up --build
```

### Development (Hot Reload)

```bash
docker compose --env-file ./backend/.env -f compose.yaml -f compose.dev.yaml up --build
```

## Project Status

This project is considered feature-complete for its first version.

There are still possible improvements, such as:

- optimizing AI prompts and output quality
- saving generated AI plans and task groups
- adding a calendar view for due tasks
- adding more tests for edge cases
- improving UI polish and animations

For now, the project is intentionally kept at this stage and will be used as a completed portfolio project. Future work will continue in separate projects to explore more advanced backend and AI engineering topics.