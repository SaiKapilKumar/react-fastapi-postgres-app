from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
import shutil
import os

router = APIRouter(
    prefix="/designer",
    tags=["Designer"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIRECTORY = "./uploaded_designs"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# POST route for uploading a design
@router.post("/{enquiry_id}", response_model=schemas.Designer)
async def upload_design(enquiry_id: int, design_file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = f"{UPLOAD_DIRECTORY}/{design_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(design_file.file, file_object)

    designer_data = schemas.DesignerCreate(
        enquiry_id=enquiry_id,
        design_file=file_location
    )

    db_designer = crud.create_designer(db, designer=designer_data)
    return db_designer

# GET route to retrieve designs for a specific enquiry
@router.get("/{enquiry_id}", response_model=schemas.Designer)
async def get_design(enquiry_id: int, db: Session = Depends(get_db)):
    db_design = crud.get_design_by_enquiry_id(db, enquiry_id=enquiry_id)
    if db_design is None:
        raise HTTPException(status_code=404, detail="Design not found")
    return db_design

# Optional: GET route to retrieve all designs
@router.get("/", response_model=list[schemas.Designer])
async def get_all_designs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    designs = crud.get_all_designs(db, skip=skip, limit=limit)
    return designs