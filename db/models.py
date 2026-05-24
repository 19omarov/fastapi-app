from sqlalchemy import Column, Integer, String, DECIMAL
from db.database import Base
class User(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    telephone = Column(String, unique=True, index=True)
    cash = Column(DECIMAL(10, 2))
