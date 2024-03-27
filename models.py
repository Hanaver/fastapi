from sqlalchemy import Column, Integer, String, DateTime, BigInteger, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base

class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(100), uniuque=True, nullable=False, comment="省/州")
    country = Column(String(100), nullable=False, comment="国家")
    country_code = Column(String(100), nullable=False, comment="国家代码")
    country_population = Column(BigInteger, nullable=False, comment="国家人口")
    data = relationship("Data", back_populates="city") # data 是关联的类名， back_populates 是指定反向访问的属性名称
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")

    __mapper_args__ = {"order_by": country_code } # 按照国家代码正序排，倒叙加上.desc()

    def __repr__(self):
        return f'{self.country}_{self.province}'

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey("city.id"), comment="所属省/直辖市") # ForeignKey 里的字符串格式不是类名.属性名 而是表明.字段名
    date = Column(Date, nullable=False, comment="数据日期")
    confirmed = Column(BigInteger, default=0, nullable=False, comment="确诊人数")
    deaths = Column(BigInteger, default=0, nullable=False, comment="死亡人数")
    recovered = Column(BigInteger, default=0, nullable=False, comment="痊愈人数")

    city = relationship("City", back_populates="data")
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间")

    __mapper_args__ = {"order_by": date.desc() }

    def __repr__(self):
        return f'{repr(self.date)}: 确证{self.confirmed}例'
    

    """
    SQLALchaemy 教程链接

    """