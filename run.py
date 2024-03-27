from typing import Union
import uvicorn
from fastapi import FastAPI
from main import app

fapp = FastAPI()
fapp.include_router(app, prefix="/api", tags=['标题信息'])

if __name__ == "__main__":
    uvicorn.run('run:app', host="127.0.0.1", port=8000, reload= True, workers=1) 
