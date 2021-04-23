from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pydantic
import uvicorn
import json

from module_access_user import user

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
# 클라이언트가 /app/signup에 접근하면 서버는 제네시스블록을 생성하는 포스트
@app.post("/app/signup")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...), clientrandom:str=Form(...)):

    result = user().genesis_block_create(user_id,user_pwd, clientrandom)
    return result

# Login API
# 클라이언트가 /app/login에 접근하면 서버는 입력한 폼(id, pw)로 로그인 검증 수행
@app.post("/app/login")
async def app_login(request:Request, user_id:str=Form(...), user_pwd:str=Form(...)):
    result = user().login(user_id, user_pwd)
    return result

# Post Access API
# 클라이언트가 /app/post에 접근하면 해당id의 다음 블록을 생성
@app.post("/app/post")
async def app_post(request:Request, user_id:str=Form(...), user_pwd:str=Form(...), postcode:str=Form(...)):
    result = user().next_block_create(user_id, user_pwd, postcode)
    return result


########################################################################################


# 자동 시작
if __name__== "__main__":
    uvicorn.run("module_start:app", host="0.0.0.0", port=55555, reload=True)
    