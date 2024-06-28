from enum import StrEnum, auto


class PatientSex(StrEnum):
    """
    Enumerator for patient sex.
    """

    MALE = auto()
    FEMALE = auto()


class MedicationForm(StrEnum):
    """
    Enumerator for medication form.
    """

    POWDER = auto()
    TABLET = auto()
    CAPSULE = auto()
    SYRUP = auto()


class MedicationStatus(StrEnum):
    """
    Enumerator for medication status.
    """

    ACTIVE = auto()
    ON_HOLD = auto()
    CANCELLED = auto()
    COMPLETED = auto()
