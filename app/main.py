from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.prompt_creator import create_prompt
#import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Allow HTML/JS on localhost to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only, allows all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_prompt(request: Request):
    body = await request.json()
    task_description = body.get("task")
    provider = body.get("provider")
    if not task_description:
        return {"error": "Please provide a 'task'"}
    if not provider:
        return {"error": "Please select a 'provider'"}
    prompt = create_prompt(task_description, provider)
    return {"prompt": prompt}