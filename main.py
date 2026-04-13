from fastapi import FastAPI, HTTPException
from routes import customers, revenue

app = FastAPI()

@app.get("/")
def home():
    return{"status": "Running"}

# include router to access routes available in other modules
app.include_router(revenue.router)
app.include_router(customers.router)

# @app.get("/revenue")
# def revenue(start_date: str, end_date: str):
#     return{"start": start_date, "end": end_date, "value": 160000}

# @app.get("/revenue")
# def get_revenue():
#     return{"month": "Jan", "Revenue": 101000}

# @app.get("/customers")
# def get_customers():
#     return[{"id": 1, "name": "ABC Corp"}]


