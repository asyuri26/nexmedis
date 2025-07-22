from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Item
import json
import os

app = FastAPI()

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = "data.json"

# Helper function
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    data = load_data()
    return templates.TemplateResponse("index.html", {"request": request, "items": data})

# Send JSON
@app.get("/send-json", response_class=JSONResponse)
async def send_json():
    sample_data = {"message": "JSON from the server", "status": "success"}
    return sample_data

# Receive JSON
@app.post("/receive-json")
async def receive_json(item: Item):
    data = load_data()
    if any(existing["id"] == item.id for existing in data):
        return JSONResponse(status_code=400, content={"message": f"ID '{item.id}' sudah ada."})
    
    data.append(item.dict())
    save_data(data)
    return {"message": "Data received and saved", "item": item}

@app.post("/modify-json")
async def modify_json(item: Item):
    data = load_data()
    for i, existing in enumerate(data):
        if existing["id"] == item.id:
            data[i] = item.dict()
            save_data(data)
            return {"message": "Data berhasil diperbarui", "item": item}
    
    return JSONResponse(status_code=404, content={"message": f"ID '{item.id}' tidak ditemukan."})