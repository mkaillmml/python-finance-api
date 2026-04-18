from fastapi import APIRouter
from app.db import get_connection

router = APIRouter()

@router.get("/customers")
def customers():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("Select CustomerName, Region from Customers")

    data = [row for row in cursor.fetchall()]
    print(data)

    data_dict = dict(data)
    print(data_dict)

    return data_dict
    
    
    #return [{"id": 1, "name": "ABC Corp"}]

