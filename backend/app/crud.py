# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
import uuid

# Enquiry CRUD operations
def create_enquiry(db: Session, enquiry: schemas.EnquiryCreate):
    enquiry_id = str(uuid.uuid4())
    db_enquiry = models.Enquiry(**enquiry.dict(), enquiry_id=enquiry_id)
    db.add(db_enquiry)
    db.commit()
    db.refresh(db_enquiry)
    return db_enquiry

def get_enquiry(db: Session, enquiry_id: int):
    return db.query(models.Enquiry).filter(models.Enquiry.id == enquiry_id).first()

def get_enquiry_by_enquiry_id(db: Session, enquiry_id: str):
    return db.query(models.Enquiry).filter(models.Enquiry.enquiry_id == enquiry_id).first()

def get_enquiries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Enquiry).offset(skip).limit(limit).all()

# Designer CRUD operations
def create_designer(db: Session, designer: schemas.DesignerCreate):
    db_designer = models.Designer(**designer.dict())
    db.add(db_designer)
    db.commit()
    db.refresh(db_designer)
    return db_designer

def get_designer(db: Session, designer_id: int):
    return db.query(models.Designer).filter(models.Designer.id == designer_id).first()

def get_designs_by_enquiry_id(db: Session, enquiry_id: int):
    return db.query(models.Designer).filter(models.Designer.enquiry_id == enquiry_id).all()

# Get all designs
def get_all_designs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Designer).offset(skip).limit(limit).all()

# Order Confirmation CRUD operations
def create_order_confirmation(db: Session, order_confirmation: schemas.OrderConfirmationCreate):
    order_id = str(uuid.uuid4())
    db_order_confirmation = models.OrderConfirmation(
        enquiry_id=order_confirmation.enquiry_id,
        po_number=order_confirmation.po_number,
        order_id=order_id
    )
    db.add(db_order_confirmation)
    db.commit()
    db.refresh(db_order_confirmation)
    return db_order_confirmation

def get_order_confirmation(db: Session, order_confirmation_id: int):
    return db.query(models.OrderConfirmation).filter(models.OrderConfirmation.id == order_confirmation_id).first()

def get_order_confirmation_by_order_id(db: Session, order_id: str):
    return db.query(models.OrderConfirmation).filter(models.OrderConfirmation.order_id == order_id).first()

# Raw Material CRUD operations
def create_raw_material(db: Session, raw_material: schemas.RawMaterialCreate):
    db_raw_material = models.RawMaterial(**raw_material.dict())
    db.add(db_raw_material)
    db.commit()
    db.refresh(db_raw_material)
    return db_raw_material

def get_raw_material(db: Session, raw_material_id: int):
    return db.query(models.RawMaterial).filter(models.RawMaterial.id == raw_material_id).first()

def get_raw_material_by_enquiry_id(db: Session, enquiry_id: int):
    return db.query(models.RawMaterial).filter(models.RawMaterial.enquiry_id == enquiry_id).first()

def update_raw_material(db: Session, raw_material_id: int, material_available: str):
    db_raw_material = get_raw_material(db, raw_material_id)
    if db_raw_material:
        db_raw_material.material_available = material_available
        db.commit()
        db.refresh(db_raw_material)
    return db_raw_material

# Process Task CRUD operations
def create_process_task(db: Session, process_task: schemas.ProcessTaskCreate):
    db_process_task = models.ProcessTask(**process_task.dict())
    db.add(db_process_task)
    db.commit()
    db.refresh(db_process_task)
    return db_process_task

def get_process_task(db: Session, process_task_id: int):
    return db.query(models.ProcessTask).filter(models.ProcessTask.id == process_task_id).first()

def get_process_tasks_by_enquiry_id(db: Session, enquiry_id: int):
    return db.query(models.ProcessTask).filter(models.ProcessTask.enquiry_id == enquiry_id).all()

def update_process_task(db: Session, process_task_id: int, quantity_returned: int, quantity_destroyed: int):
    db_process_task = get_process_task(db, process_task_id)
    if db_process_task:
        db_process_task.quantity_returned = quantity_returned
        db_process_task.quantity_destroyed = quantity_destroyed
        db.commit()
        db.refresh(db_process_task)
    return db_process_task