from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json

from module_access_user import USER

# http://112.156.0.196:55555
# Fastapi function start
app = FastAPI()

# CORS Setting
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static management
#app.mount("/static", StaticFiles(directory='static'), name='static')
#templates = Jinja2Templates(directory='templates')


# Access API Management
# Signup API
@app.post("/app/signup")
async def appSignup(request:Request, userId:str=Form(...), userPwd:str=Form(...), clientRandom:str=Form(...)):

    result = user().genesisBlockCreate(userId,userPwd, clientRandom)
    return result

# Login API
@app.post("/app/login")
async def appLogin(request:Request, userId:str=Form(...), userPwd:str=Form(...)):
    result = user().login(userId, userPwd)
    return result

# Post Access API
@app.post("/app/post")
async def appPost(request:Request, userId:str=Form(...), userPwd:str=Form(...), postCode:str=Form(...)):
    result = user().nextBlockCreate(userId, userPwd, postCode)
    return result


########################################################################################


# 자동 시작
if __name__== "__main__":
    uvicorn.run("module_start:app", host="0.0.0.0", port=55555, reload=True)
    
