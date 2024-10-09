from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/raw-materials",
    tags=["Raw Materials"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create raw material (POST)
@router.post("/", response_model=schemas.RawMaterial)
def create_raw_material(raw_material: schemas.RawMaterialCreate, db: Session = Depends(get_db)):
    return crud.create_raw_material(db=db, raw_material=raw_material)

# Update raw material by ID (PUT)
@router.put("/{raw_material_id}", response_model=schemas.RawMaterial)
def update_raw_material(raw_material_id: int, material_available: schemas.RawMaterialUpdate, db: Session = Depends(get_db)):
    db_raw_material = crud.get_raw_material(db, raw_material_id)
    if db_raw_material is None:
        raise HTTPException(status_code=404, detail="Raw material not found")
    return crud.update_raw_material(db=db, raw_material_id=raw_material_id, material_available=material_available.material_available)

# Check raw material availability by enquiry ID (GET)
@router.get("/{enquiry_id}", response_model=schemas.RawMaterial)
def check_raw_material_by_enquiry_id(enquiry_id: int, db: Session = Depends(get_db)):
    raw_material = crud.get_raw_material_by_enquiry_id(db=db, enquiry_id=enquiry_id)
    if raw_material is None:
        raise HTTPException(status_code=404, detail="Raw material not found")
    return raw_material