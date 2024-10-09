# backend/app/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Enquiry Schemas
class EnquiryBase(BaseModel):
    customer_name: str
    customer_code: str
    date: date
    required_material: str
    quantity: int

class EnquiryCreate(EnquiryBase):
    pass

class Enquiry(EnquiryBase):
    id: int
    enquiry_id: str

    class Config:
        orm_mode = True

# Designer Schemas
class DesignerBase(BaseModel):
    enquiry_id: int
    design_file: str  # This could be a file path or URL

class DesignerCreate(BaseModel):
    enquiry_id: int
    design_file: Optional[str] = None  # To handle file uploads

class Designer(DesignerBase):
    id: int

    class Config:
        orm_mode = True

# Order Confirmation Schemas
class OrderConfirmationBase(BaseModel):
    enquiry_id: int
    po_number: str
    order_id: str

class OrderConfirmationCreate(BaseModel):
    enquiry_id: int
    po_number: str

class OrderConfirmation(OrderConfirmationBase):
    id: int

    class Config:
        orm_mode = True


# Base schema for raw materials
class RawMaterialBase(BaseModel):
    enquiry_id: int
    material_available: str  # "Yes" or "No"

# Schema for creating raw material
class RawMaterialCreate(RawMaterialBase):
    pass

# Schema for updating raw material availability
class RawMaterialUpdate(BaseModel):
    material_available: str

# Response model for raw materials
class RawMaterial(RawMaterialBase):
    id: int

    class Config:
        orm_mode = True

# Process Task Schemas
class ProcessTaskBase(BaseModel):
    enquiry_id: int
    quantity_given: int
    quantity_returned: int
    quantity_destroyed: int

class ProcessTaskCreate(BaseModel):
    enquiry_id: int
    quantity_given: int
    quantity_returned: int
    quantity_destroyed: int

class ProcessTask(ProcessTaskBase):
    id: int

    class Config:
        orm_mode = True