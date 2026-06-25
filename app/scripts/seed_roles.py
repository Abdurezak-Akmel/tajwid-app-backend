from sqlalchemy.orm import Session
from app.modules.roles.repository import RoleRepository
from app.modules.roles.models import Role

def seed_roles(db: Session):
    """
    Seed initial roles with fixed IDs. 
    1: admin, 2: user
    """
    roles_to_seed = [
        {"id": 1, "name": "admin", "access_details": {"all": True}},
        {"id": 2, "name": "user", "access_details": {"all": False}},
    ]
    
    print("--- Checking Roles ---")
    for role_data in roles_to_seed:
        # Check by ID to ensure consistency
        existing_role = db.query(Role).filter(Role.id == role_data["id"]).first()
        if not existing_role:
            # Check if name is already used by another ID (safety check)
            name_check = db.query(Role).filter(Role.name == role_data["name"]).first()
            if not name_check:
                db_role = Role(**role_data)
                db.add(db_role)
                db.commit()
                print(f"Created role: {role_data['name']} (ID: {role_data['id']})")
            else:
                print(f"Role name '{role_data['name']}' exists with different ID. Skipping.")
        else:
            print(f"Role ID {role_data['id']} ({role_data['name']}) already exists.")
