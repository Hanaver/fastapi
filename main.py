from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import curd, schemas
from database import SessionLocal, engine, Base
from models import City, Data

application = APIRouter()

templates = Jinja2Templates(directory = './templates')

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@application.post("/create_city", response_model=schemas.ReadCity)
def create_city(city: schemas.CreateCity, db: Session = Depends(get_db)):
    db_city = curd.get_city_by_name(db=db, name=city.province)
    if db_city:
        raise HTTPException(status_code=404, detail='City is aleady')
    return curd.create_city(db=db, city=city)


@application.get('/' , response_class=HTMLResponse)
def home(request: Request, city: str = None):
    return templates.TemplateResponse(
        request=request,
        name= 'home.html'
    )