from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- passlib/bcrypt Compatibility Patch ---
import logging
# This fixes "AttributeError: module 'bcrypt' has no attribute '__about__'"
try:
    import bcrypt
    if not hasattr(bcrypt, "__about__"):
        bcrypt.__about__ = type("about", (object,), {"__version__": bcrypt.__version__})
except ImportError:
    pass
# ------------------------------------------

from app.database.session import SessionLocal
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as user_router
from app.modules.roles.router import router as role_router

from app.scripts.seed_roles import seed_roles
from app.scripts.seed_admin import seed_admin

# 1. Lifespan Event Handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Executes tasks on server startup and shutdown.
    """
    # STARTUP LOGIC: Seed Initial Data
    db = SessionLocal()
    try:
        seed_roles(db)
        seed_admin(db)
    finally:
        db.close()
        
    yield
    
    # SHUTDOWN LOGIC: (None at the moment)

# 2. App Initialization
app = FastAPI(
    title="Tejwid App API",
    description="Comprehensive Backend API for the Tejwid Mobile Learning Application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# 3. CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Register Active Routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)

# 5. System Status Endpoints
@app.get("/health", tags=["System"])
def health_check():
    """System health check endpoint."""
    return {
        "status": "online",
        "api_version": "1.0.0",
        "environment": "development"
    }
