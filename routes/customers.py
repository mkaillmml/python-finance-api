from fastapi import APIRouter

router = APIRouter()

@router.get("/customers")
def customers():
    return [{"id": 1, "name": "ABC Corp"}]

