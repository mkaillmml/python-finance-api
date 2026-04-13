from fastapi import APIRouter
from services.revenue_service import get_revenue_data

router = APIRouter()

@router.get("/revenue")
def revenue():
    return get_revenue_data()

