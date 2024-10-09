# backend/app/routers/process.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal

router = APIRouter(
    prefix="/process",
    tags=["Process"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProcessTask)
def create_process_task(task: schemas.ProcessTaskCreate, db: Session = Depends(get_db)):
    db_task = crud.create_process_task(db, process_task=task)
    return db_task

@router.put("/{task_id}", response_model=schemas.ProcessTask)
def update_process_task(task_id: int, quantity_returned: int, quantity_destroyed: int, db: Session = Depends(get_db)):
    db_task = crud.update_process_task(db, process_task_id=task_id, quantity_returned=quantity_returned, quantity_destroyed=quantity_destroyed)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Process task not found")
    return db_task