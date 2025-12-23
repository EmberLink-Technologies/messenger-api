# Messenger API

Backend API for the Messenger project.

Built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Alembic (migrations)
- JWT (PyJWT)
- Argon2 (password hashing)

---

## Project Structure

```
app/
├── core/
│   ├── config.py
│   ├── database.py
│   ├── token.py
│   └── passwords.py
│
├── models/
│   └── account.py
│
├── schemas/
│   ├── account.py
│   └── token.py
│
├── handlers/
│   └── account.py
│
├── routers/
│   ├── auth.py
│   └── account.py
│
├── main.py
└── alembic/
```

---

## Architecture Rules

- Routers → HTTP layer only
- Handlers → business logic
- Schemas → validation
- Models → database tables
- Core → shared infrastructure

---

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost/messenger_db
SECRET_KEY=change_me
ALGORITHM=HS256
```

Run migrations:

```bash
alembic upgrade head
```

Start server:

```bash
uvicorn app.main:app --reload
```

---

## Auth

### Register
POST `/auth/register`

### Login
POST `/auth/token`

Authorization header:
```
Bearer <access_token>
```

---

## Endpoints

- GET `/users/me`
- GET `/users/{user_id}`

---

## TODO

- Refresh tokens
- User update/delete
- Tests
- Messaging module