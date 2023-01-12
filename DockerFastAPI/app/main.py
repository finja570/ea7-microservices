from fastapi import FastAPI, Request
import random
import string
from app import dog_data
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./app/html")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/password")    
def randomString(request: Request, length: int):
    letters = string.ascii_lowercase
    generated_password = ''.join(random.choice(letters) for i in range(length))
    return templates.TemplateResponse("password.html", {"request": request, "password": generated_password})

@app.get("/random-dog")
async def random_dog(request: Request):
    dog = await dog_data.get_dog()
    if not dog:
        raise fastapi.HTTPException(satus_code=404)

    dog_url = dog["url"]    

    return templates.TemplateResponse("random_dog.html", {"request": request, "url": dog_url})

    

