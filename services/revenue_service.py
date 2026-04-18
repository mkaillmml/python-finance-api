from app.db import get_connection

def get_revenue_data():
    conn = get_connection()
    cursor = conn.cursor()
    print(cursor)

    cursor.execute("Select TOP 3 * from Revenue")

    print("Here1")
    data = [row for row in cursor.fetchall()]
    print("here2")
    conn.close()
    print("here3")
    print(data)

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