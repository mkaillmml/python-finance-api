from app.db import get_connection
import json

def get_revenue_data():
    conn = get_connection()
    cursor = conn.cursor()
    print(cursor)

    cursor.execute("Select * from Revenue")

    #data = [row for row in cursor.fetchall()]
    rows = cursor.fetchall()
    conn.close()
    #print(data)

    print(rows)

    dt = json.dumps([list(i) for i in rows]) # Create JSON
    print(dt)

    return dt


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