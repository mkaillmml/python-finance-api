from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return{"status": "Running"}

@app.get("/revenue")
def get_revenue():
    return{"month": "Jan", "Revenue": 101000}

@app.get("/customers")
def get_customers():
    return[{"id": 1, "name": "ABC Corp"}]