# backend/app/routers/order.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderConfirmation)
def create_order(order: schemas.OrderConfirmationCreate, db: Session = Depends(get_db)):
    db_order = crud.create_order_confirmation(db, order_confirmation=order)
    return db_order

@router.get("/{order_id}", response_model=schemas.OrderConfirmation)
def read_order(order_id: str, db: Session = Depends(get_db)):
    db_order = crud.get_order_confirmation_by_order_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order