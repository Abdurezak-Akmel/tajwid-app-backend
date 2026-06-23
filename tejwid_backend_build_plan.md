<!--# Tejwid App — Backend Build Plan -->

> [!IMPORTANT]
> **Current Status:** Only [main.py](file:///d:/Tejwid%20App/tejwid-mob-app/main.py) has code (a basic FastAPI hello-world). **Every other file in the project is empty.** The folder structure is well-organized scaffolding — now you need to fill it in from the ground up.

---

## 📁 Project Structure Overview

```
tejwid-mob-app/
├── main.py                     # FastAPI entry point (exists, minimal)
├── core/                       # App-wide configuration & security
│   ├── config.py               # ⬜ Settings, env vars
│   ├── constants.py            # ⬜ App-wide constants
│   ├── exceptions.py           # ⬜ Custom exception classes
│   ├── logging.py              # ⬜ Logging configuration
│   ├── permissions.py          # ⬜ Permission / role guards
│   └── security.py             # ⬜ JWT, hashing, token utilities
├── database/                   # Database layer
│   ├── base.py                 # ⬜ SQLAlchemy Base model
│   ├── session.py              # ⬜ Engine + async session factory
│   └── migrations/             # ⬜ Alembic migrations (empty)
├── common/                     # Shared utilities
│   ├── dependencies.py         # ⬜ FastAPI Depends (get_db, get_current_user)
│   ├── enums.py                # ⬜ Shared enums (UserRole, Status, etc.)
│   ├── pagination.py           # ⬜ Pagination helpers
│   ├── responses.py            # ⬜ Standard API response models
│   └── validators.py           # ⬜ Shared validators
├── modules/                    # Feature modules (each: schemas, router, service, repository, utils)
│   ├── auth/                   # ⬜ Login, register, token refresh
│   ├── users/                  # ⬜ User profile CRUD
│   ├── roles/                  # ⬜ Role management
│   ├── admin/                  # ⬜ Admin-specific endpoints
│   ├── courses/                # ⬜ Course CRUD
│   ├── chapters/               # ⬜ Chapter CRUD (per course)
│   ├── tajwid_rules/           # ⬜ Tajwid rules catalog
│   ├── videos/                 # ⬜ Video lesson management
│   ├── quizzes/                # ⬜ Quizzes & questions
│   ├── progress/               # ⬜ User progress tracking
│   ├── payments/               # ⬜ Payment / subscription logic
│   ├── notifications/          # ⬜ Push / in-app notifications
│   └── downloads/              # ⬜ Downloadable material
├── storage/                    # External storage integration
│   ├── supabase.py             # ⬜ Supabase client setup
│   └── file_service.py         # ⬜ File upload/download abstraction
├── background_tasks/           # Async / scheduled jobs
│   ├── cleanup_tasks.py        # ⬜ Old data cleanup
│   ├── email_tasks.py          # ⬜ Email sending
│   └── notification_tasks.py   # ⬜ Push notification dispatch
├── scripts/                    # One-off / seed scripts
│   ├── seed_admin.py           # ⬜ Create initial admin user
│   ├── seed_courses.py         # ⬜ Populate courses data
│   └── seed_roles.py          # ⬜ Populate roles
└── tests/                      # Test suites
    ├── auth/                   # ⬜ Auth tests
    └── courses/                # ⬜ Course tests
```

> **Legend:** ⬜ = empty file, needs implementation

---

## 🚀 Build Steps (Recommended Order)

### Phase 1: Foundation (Do this first — everything depends on it)

| Step | File(s) | What to Do |
|------|---------|------------|
| **1.1** | `pyproject.toml` or `requirements.txt` | Create a dependency manifest. Key packages: `fastapi`, `uvicorn[standard]`, `sqlalchemy[asyncio]`, `asyncpg` (or `aiosqlite` for dev), `alembic`, `pydantic-settings`, `python-jose[cryptography]`, `passlib[bcrypt]`, `supabase` |
| **1.2** | [core/config.py](file:///d:/Tejwid%20App/tejwid-mob-app/core/config.py) | Define `Settings` class using `pydantic-settings`. Load `DATABASE_URL`, `SECRET_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES`, etc. from a `.env` file |
| **1.3** | `.env` + `.env.example` | Create your actual `.env` (gitignored) and a committed `.env.example` template |
| **1.4** | [core/constants.py](file:///d:/Tejwid%20App/tejwid-mob-app/core/constants.py) | Define app-wide constants (API version prefix, default page sizes, etc.) |
| **1.5** | [core/logging.py](file:///d:/Tejwid%20App/tejwid-mob-app/core/logging.py) | Configure structured logging (use Python's `logging` module or `loguru`) |
| **1.6** | [core/exceptions.py](file:///d:/Tejwid%20App/tejwid-mob-app/core/exceptions.py) | Define custom exceptions (`NotFoundException`, `ForbiddenException`, `BadRequestException`) and register FastAPI exception handlers |

### Phase 2: Database Layer

| Step | File(s) | What to Do |
|------|---------|------------|
| **2.1** | [database/base.py](file:///d:/Tejwid%20App/tejwid-mob-app/database/base.py) | Define `Base = declarative_base()` and a `BaseModel` mixin with `id`, `created_at`, `updated_at` columns |
| **2.2** | [database/session.py](file:///d:/Tejwid%20App/tejwid-mob-app/database/session.py) | Create async engine + `AsyncSessionLocal` session factory. Provide a `get_db` async generator |
| **2.3** | `database/migrations/` | Initialize Alembic (`alembic init database/migrations`), configure `env.py` to use your `Base.metadata` and `DATABASE_URL` |
| **2.4** | `common/enums.py` | Define enums: `UserRole` (admin, teacher, student), `CourseStatus`, `PaymentStatus`, `ProgressStatus`, etc. |

### Phase 3: Auth & Security (Gate to every other module)

| Step | File(s) | What to Do |
|------|---------|------------|
| **3.1** | `core/security.py` | Implement: `hash_password()`, `verify_password()`, `create_access_token()`, `create_refresh_token()`, `decode_token()` |
| **3.2** | `modules/users/schemas.py` | Define `UserCreate`, `UserRead`, `UserUpdate` Pydantic models |
| **3.3** | `modules/users/repository.py` | Define the `User` SQLAlchemy model + DB queries (get_by_id, get_by_email, create, update) |
| **3.4** | `modules/users/service.py` | Business logic layer wrapping the repository |
| **3.5** | `modules/users/router.py` | CRUD endpoints: `GET /users/me`, `PATCH /users/me`, admin: `GET /users`, `GET /users/{id}` |
| **3.6** | `modules/auth/schemas.py` | `LoginRequest`, `RegisterRequest`, `TokenResponse`, `RefreshRequest` |
| **3.7** | `modules/auth/repository.py` | Token storage / refresh token management (if storing in DB) |
| **3.8** | `modules/auth/service.py` | `register()`, `login()`, `refresh_token()`, `logout()` |
| **3.9** | `modules/auth/router.py` | `POST /auth/register`, `POST /auth/login`, `POST /auth/refresh`, `POST /auth/logout` |
| **3.10** | `common/dependencies.py` | `get_current_user` dependency (decode JWT → fetch user), `get_db` session dependency |
| **3.11** | `core/permissions.py` | Role-based permission decorators/dependencies: `require_role(UserRole.admin)`, `require_role(UserRole.teacher)` |
| **3.12** | `modules/roles/` | Role CRUD if roles are dynamic (schemas → repository → service → router) |

### Phase 4: Core Business Modules

Build these in dependency order — courses first, then chapters, then the rest.

#### 4A. Courses
| Step | File(s) | What to Do |
|------|---------|------------|
| **4A.1** | `modules/courses/schemas.py` | `CourseCreate`, `CourseRead`, `CourseUpdate`, `CourseListResponse` |
| **4A.2** | `modules/courses/repository.py` | `Course` SQLAlchemy model + queries |
| **4A.3** | `modules/courses/service.py` | Business logic (create, list with pagination, get by ID, update, delete) |
| **4A.4** | `modules/courses/router.py` | `GET /courses`, `POST /courses` (admin), `GET /courses/{id}`, `PATCH /courses/{id}`, `DELETE /courses/{id}` |

#### 4B. Chapters
| Step | File(s) | What to Do |
|------|---------|------------|
| **4B.1** | `modules/chapters/` | Same pattern. Chapters belong to a course (`course_id` FK). Endpoints nested: `GET /courses/{id}/chapters`, etc. |

#### 4C. Tajwid Rules
| Step | File(s) | What to Do |
|------|---------|------------|
| **4C.1** | `modules/tajwid_rules/` | Catalog of tajwid rules. Each rule has a name (Arabic + transliteration), description, audio example reference, and related chapter(s) |

#### 4D. Videos
| Step | File(s) | What to Do |
|------|---------|------------|
| **4D.1** | `modules/videos/` | Video metadata linked to chapters. Actual files stored via Supabase Storage |

### Phase 5: Storage Layer

| Step | File(s) | What to Do |
|------|---------|------------|
| **5.1** | `storage/supabase.py` | Initialize Supabase client from `core/config.py` settings |
| **5.2** | `storage/file_service.py` | Implement `upload_file()`, `get_file_url()`, `delete_file()` using Supabase Storage buckets |

### Phase 6: Engagement & Monetization Modules

| Step | File(s) | What to Do |
|------|---------|------------|
| **6.1** | `modules/quizzes/` | Quiz model (belongs to chapter), Question model, Answer model. Endpoints for taking quizzes and grading |
| **6.2** | `modules/progress/` | Track per-user progress (course %, chapter completion, quiz scores). Endpoints: `POST /progress/complete-chapter`, `GET /progress/course/{id}` |
| **6.3** | `modules/payments/` | Payment/subscription management. Integrate with a payment gateway (Chapa, Stripe, etc.) |
| **6.4** | `modules/downloads/` | Downloadable PDFs, audio files. Reference storage layer for serving files |
| **6.5** | `modules/notifications/` | Notification model + endpoints. `GET /notifications`, `PATCH /notifications/{id}/read` |

### Phase 7: Admin Module

| Step | File(s) | What to Do |
|------|---------|------------|
| **7.1** | `modules/admin/` | Admin dashboard stats (`GET /admin/stats`), user management, course approval workflows. Reuses other module services with admin permission guards |

### Phase 8: Background Tasks & Scripts

| Step | File(s) | What to Do |
|------|---------|------------|
| **8.1** | `background_tasks/email_tasks.py` | Email sending (welcome email, password reset). Use `fastapi.BackgroundTasks` or Celery |
| **8.2** | `background_tasks/notification_tasks.py` | Push notification dispatch (Firebase Cloud Messaging) |
| **8.3** | `background_tasks/cleanup_tasks.py` | Periodic cleanup (expired tokens, old notifications) |
| **8.4** | `scripts/seed_roles.py` | Script to seed default roles into the DB |
| **8.5** | `scripts/seed_admin.py` | Script to create the first admin user |
| **8.6** | `scripts/seed_courses.py` | Script to populate sample course data |

### Phase 9: Shared Utilities & Polish

| Step | File(s) | What to Do |
|------|---------|------------|
| **9.1** | `common/pagination.py` | Generic pagination helper: `paginate(query, page, size)` → `PaginatedResponse` |
| **9.2** | `common/responses.py` | Standard response wrappers: `SuccessResponse`, `ErrorResponse` |
| **9.3** | `common/validators.py` | Reusable validators (email format, phone, Arabic text validation) |

### Phase 10: Wire Everything into `main.py`

| Step | File(s) | What to Do |
|------|---------|------------|
| **10.1** | `main.py` | Import & include all routers, register exception handlers, add CORS middleware, configure lifespan events (DB init), mount Swagger docs |

### Phase 11: Testing

| Step | File(s) | What to Do |
|------|---------|------------|
| **11.1** | `tests/` | Write tests for each module. Start with auth (register, login, token refresh), then courses CRUD. Use `pytest` + `httpx` `AsyncClient` |

---

## 🧩 Module Internal Pattern

Every module follows the same 5-file pattern:

```
modules/<feature>/
├── schemas.py      → Pydantic models (request/response DTOs)
├── repository.py   → SQLAlchemy model + raw DB operations
├── service.py      → Business logic (calls repository)
├── router.py       → FastAPI router (calls service)
└── utils.py        → Module-specific utilities
```

> [!TIP]
> **Always build in this order within each module:** `schemas.py` → `repository.py` → `service.py` → `router.py` → `utils.py`

---

## ⚡ Quick-Start Checklist

- [ ] Create `requirements.txt` / `pyproject.toml`
- [ ] Install dependencies in your `.venv`
- [ ] Create `.env` with database URL + secrets
- [ ] Implement `core/config.py`
- [ ] Implement `database/base.py` + `database/session.py`
- [ ] Initialize Alembic
- [ ] Build Auth module (security → users → auth)
- [ ] Build Courses module
- [ ] Connect routers in `main.py`
- [ ] Run first migration + test

> [!CAUTION]
> You have **no `requirements.txt` or `pyproject.toml`** yet. Create one before anything else, so your dependencies are tracked and reproducible.
