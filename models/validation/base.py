from pydantic import BaseModel
import uuid
import datetime


class BaseValidationModel(BaseModel):
    """
    Base validation model for all models.
    """

    id_: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True
