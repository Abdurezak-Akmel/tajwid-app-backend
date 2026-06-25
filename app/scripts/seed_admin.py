from sqlalchemy.orm import Session
from app.modules.users.service import UserService
from app.modules.users.schemas import UserCreate
from app.core.exceptions import ConflictError

def seed_admin(db: Session):
    """
    Seed initial admin user.
    """
    user_service = UserService(db)
    
    admin_data = UserCreate(
        full_name="System Admin",
        email="admin@tejwid.com",
        password="admin123",
        role_id=1,  # Matches the ID set in seed_roles
        tg_username="@sys_admin",
        is_verified=True
    )
    
    print("--- Checking Admin User ---")
    try:
        if not user_service.get_user_by_email(admin_data.email):
            user_service.create_user(admin_data)
            print(f"Admin user created: {admin_data.email}")
        else:
            print(f"Admin user already exists: {admin_data.email}")
    except Exception as e:
        print(f"Error seeding admin: {e}")
