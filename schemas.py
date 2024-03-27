# 建立模型里对应的数据格式类
from datetime import datetime
from datetime import date as date_
from pydantic import BaseModel

class CreateCity(BaseModel):
    province: str
    country: str
    country_code: str
    country_population: int

class CreateData(BaseModel):
    date: date_
    confirmed: int = 0
    deaths: int = 0
    recovered: int = 0


class ReadCity(CreateCity):
    id: int
    province: str
    country: str
    country_code: str
    country_population: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ReadData(CreateData):
    id: int
    city_id: int
    date: date_
    confirmed: int
    deaths: int
    recovered: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True