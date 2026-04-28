from app.db import get_connection
import json

cache = {}

def get_revenue_cached():
    if "revenue" in cache:
        return cache["revenue"]
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("Select SUM(Revenue) from Revenue")

    value = cursor.fetchone()[0]
    result = {"revenue": value}

    cache["revenue"] = result

    return result

    

def get_revenue_data():
    conn = get_connection()
    cursor = conn.cursor()
    print(cursor)

    cursor.execute("Select * from Revenue FOR JSON PATH")

    data = [row for row in cursor.fetchone()]
    #rows = cursor.fetchall()
    conn.close()
    #print(data)

    print(data)
    #print(rows)

    #dt = json.dumps([list(i) for i in rows]) # Create JSON
    #print(dt)

    return data


    # data_as_dict = data.mappings().all()
    # print(data_as_dict)
    
    data_dict = dict(data)
    print(data_dict)
    
    return data_dict    
    
    
    #return{"month": "Jan", "revenue": 120000}

def get_revenue_trend():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT Month, SUM(Revenue)
                        FROM Revenue
                        GROUP BY Month
                   """)
    
    return [{"month": r[0], "amount": r[1]} for r in cursor.fetchall()]