from fastapi import APIRouter

router = APIRouter(prefix="/medications", tags=["Medications"])


@router.get("/")
async def get_medications():
    """
    Get all medications.
    """
    return {"message": "Get all medications."}
