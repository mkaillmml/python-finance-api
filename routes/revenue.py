from fastapi import APIRouter
from services.revenue_service import get_revenue_data, get_revenue_trend, get_revenue_cached

router = APIRouter()

@router.get("/revenue")
def revenue():
    return get_revenue_cached() #get_revenue_data()

@router.get("/revenue-trend")
def revenue_trend():
    return get_revenue_trend()