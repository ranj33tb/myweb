from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from vehicle import get_vehicle_info   # make sure vehicle.py has get_vehicle_info()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})


@app.get("/contribute", response_class=HTMLResponse)
async def contribute(request: Request):
    return templates.TemplateResponse("contribute.html", {"request": request})


@app.get("/search/{vehicle_number}")
async def search(vehicle_number: str):
    try:
        return JSONResponse(get_vehicle_info(vehicle_number.upper()))
    except Exception as e:
        return JSONResponse({"error": str(e)})
