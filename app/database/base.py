from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
    The master base class for all SQLAlchemy database models.
    All models (e.g., User, Quiz, Verse) will inherit from this class.
    """
    pass

# Importing all models here
from app.modules.users.models import User
from app.modules.access_requests.models import AccessRequest
# from app.modules.auth.models import Auth
from app.modules.chapters.models import Chapter
from app.modules.courses.models import Course
from app.modules.downloads.models import Download
from app.modules.notifications.models import Notification
# from app.modules.payments.models import Payment
from app.modules.progress.models import Progress
from app.modules.quizzes.models import Quiz
from app.modules.role_course.models import RoleCourse
from app.modules.roles.models import Role
from app.modules.tajwid_rules.models import TajwidRule
from app.modules.videos.models import Video