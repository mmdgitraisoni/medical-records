from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from database.db import Base

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    scheduled_time = Column(DateTime)
    status = Column(String, default="Scheduled")
