
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
# import pymysql


# SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.sqlite3'
SQLALCHEMY_MYSQL_URI = 'mysql+pymysql://root:htq888@127.0.0.1:3306/fasapi'    # mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

engine = create_engine(SQLALCHEMY_MYSQL_URI, echo=True, connect_args={"check_same_thread": False})

# 创建DBSession类型
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=True)

# 创建基本的映射类
Base = declarative_base(metadata=engine, name="Base")

