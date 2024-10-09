# backend/app/routers/enquiry.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/enquiries",
    tags=["Enquiries"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Enquiry)
def create_enquiry(enquiry: schemas.EnquiryCreate, db: Session = Depends(get_db)):
    return crud.create_enquiry(db=db, enquiry=enquiry)

@router.get("/{enquiry_id}", response_model=schemas.Enquiry)
def read_enquiry(enquiry_id: int, db: Session = Depends(get_db)):
    db_enquiry = crud.get_enquiry(db, enquiry_id=enquiry_id)
    if db_enquiry is None:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return db_enquiry

@router.get("/", response_model=list[schemas.Enquiry])
def read_enquiries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enquiries = crud.get_enquiries(db, skip=skip, limit=limit)
    return enquiries