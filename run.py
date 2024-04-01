from typing import Union
import uvicorn
from fastapi import FastAPI
from main import application

app = FastAPI()
app.include_router(application, prefix="/api", tags=['标题信息'])

if __name__ == "__main__":
    uvicorn.run('run:app', host="0.0.0.0", port=8000, reload= True, workers=1) 
