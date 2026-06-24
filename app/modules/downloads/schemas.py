from pydantic import BaseModel, ConfigDict

class DownloadBase(BaseModel):
    """
    Base Pydantic model for Download, containing shared fields.
    """
    user_id: int
    video_id: int

class DownloadCreate(DownloadBase):
    """
    Pydantic model for creating a new download record.
    """
    pass

class Download(DownloadBase):
    """
    Pydantic model for download response, including the generated ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
