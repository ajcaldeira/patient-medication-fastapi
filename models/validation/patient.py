from models.validation.base import BaseValidationModel
from models.enumerators.common import PatientSex
import datetime


class Patient(BaseValidationModel):
    """
    Validation model for the patient.
    """

    first_name: str
    last_name: str
    date_of_birth: datetime.datetime
    sex: PatientSex
