from typing import Union
from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data
        
    

@app.get('/')
def read_root():
    return {"message": "Welcom to the FastAPI application!"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get('/views')
def get_patients():
    data = load_data()
    return data