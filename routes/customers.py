from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter()

@router.get("/customers")
def customers(region = None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "Select CustomerName From Customers"
        if region:
            query += f" Where Region = '{region}'"

        cursor.execute(query)

        return[row[0] for row in cursor.fetchall()]

    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))


    #2nd
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("Select CustomerName, Region from Customers")

    data = [row for row in cursor.fetchall()]
    print(data)

    data_dict = dict(data)
    print(data_dict)

    return data_dict
    """

    #1st
    #return [{"id": 1, "name": "ABC Corp"}]

