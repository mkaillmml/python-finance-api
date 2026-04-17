import pyodbc
from fastapi import FastAPI


def get_connection():
    print(pyodbc.drivers())

    DRIVER_NAME = 'SQL Server'
    SERVER_NAME = 'M'
    DATABASE_NAME = 'PythonProject'

    connection_string = f"""
                        DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
                        Trust_Connection=yes;
                        """
    conn = pyodbc.connect(connection_string)
    print(conn)
    return conn

    # return pyodbc.connect(
    #         "DRIVER={SQL Server};"
    #         "SERVER=M;"
    #         "DATABASE=PythonProject;"
    # )


# DRIVER_NAME = 'SQL Server'
# SERVER_NAME = 'M'
# DATABASE_NAME = 'PythonProject'

# connection_string = f"""
#                     DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
#                     Trust_Connection=yes;
#                     """
# conn = pyodbc.connect(connection_string)
# print(conn)

# cursor = conn.cursor()
# cursor.execute("Select * from Customers")

# row = cursor.fetchone()

# while row:
#     print(row)
#     row = cursor.fetchone()

#def get_connection():





    # return pyodbc.connect(
    #         "DRIVER={ODBC Driver 17 for SQL Server};"
    #         "SERVER=localhost;"
    #         "DATABASE=PythonProject;"
    # )