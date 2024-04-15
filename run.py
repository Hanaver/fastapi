from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from main import application

app = FastAPI()

# 静态文件目录配置
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(application, prefix="/api", tags=['标题信息'])

if __name__ == "__main__":
    uvicorn.run('run:app', host="127.0.0.1", port=8000, reload= True, workers=1) 
