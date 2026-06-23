from fastapi import HTTPException, status

class AppBaseException(HTTPException):
    """Base exception for all application errors."""
    def __init__(self, status_code: int, detail: str = None, headers: dict = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class NotFoundError(AppBaseException):
    """404 Not Found error."""
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class ConflictError(AppBaseException):
    """409 Conflict error — useful for duplicate entries like emails."""
    def __init__(self, detail: str = "Resource already exists"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)

class UnauthenticatedError(AppBaseException):
    """401 Unauthorized error."""
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )

class ForbiddenError(AppBaseException):
    """403 Forbidden error."""
    def __init__(self, detail: str = "Not enough permissions"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

class BadRequestError(AppBaseException):
    """400 Bad Request error."""
    def __init__(self, detail: str = "Invalid request"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class DatabaseError(AppBaseException):
    """500 Internal Server error related to database operations."""
    def __init__(self, detail: str = "A database error occurred"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
