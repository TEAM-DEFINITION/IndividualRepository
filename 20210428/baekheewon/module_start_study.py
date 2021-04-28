from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json

from module_access_user_study import user

## Fastapi function start
# Fastapi 객체 생성
app = FastAPI()

## CORS Setting
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

## static management
## app.mount("/static", StaticFiles(directory='static'), name='static')
## templates = Jinja2Templates(directory='templates')


## Access API Management
## Signup API # 사용자가 회원가입을 하면 제네시스 블록을 생성하는 api
@app.post("/app/signup")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...), clientrandom:str=Form(...)):

    # user_id, user_pwd, clientrandom을 가지고 제네시스 블록을 생성
    result = user().genesis_block_create(user_id,user_pwd, clientrandom)
    return result

## Login API # 사용자가 로그인을 진행하는 로그인을 검증하는 api
@app.post("/app/login")
async def app_login(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    result = user().login(user_id, user_pwd)
    return result

## Post Access API # postcode를 사용하여 다음 블록을 생성하는 api
@app.post("/app/post")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...), postcode:str=Form(...)):
    result = user().next_block_create(user_id, user_pwd, postcode)
    return result
    

########################################################################################


## 자동 시작
if __name__== "__main__":
    uvicorn.run("module_start:app", host="0.0.0.0", port=55555, reload=True)
    