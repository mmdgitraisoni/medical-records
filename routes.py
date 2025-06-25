from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.patient import Patient

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients/")
def create_patient(name: str, date_of_birth: str, gender: str, contact_info: str, address: str, db: Session = Depends(get_db)):
    patient = Patient(name=name, date_of_birth=date_of_birth, gender=gender, contact_info=contact_info, address=address)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient
