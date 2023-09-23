from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
from fastapi.staticfiles import StaticFiles  # Add this import

app = FastAPI()

# Serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Generate a random 3-digit code
# secret_code = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
secret_code = '436'
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, message: str = ""):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

@app.post("/")
async def guess_code(request: Request, guess: str = Form(...)):
    if guess == secret_code:
        message = "Congratulations! You guessed the correct code."
    else:
        message = "Sorry, try again. Your guess was incorrect."

    return templates.TemplateResponse("index.html", {"request": request, "message": message})
