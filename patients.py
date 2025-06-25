from sqlalchemy import Column, Integer, String, Date
from database.db import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String)
    contact_info = Column(String)
    address = Column(String)
