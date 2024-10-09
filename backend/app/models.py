# backend/app/models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Enquiry(Base):
    __tablename__ = "enquiries"
    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(String, unique=True, index=True)
    customer_name = Column(String)
    customer_code = Column(String)
    date = Column(Date)
    required_material = Column(String)
    quantity = Column(Integer)

    designer = relationship("Designer", back_populates="enquiry", uselist=False)
    order_confirmation = relationship("OrderConfirmation", back_populates="enquiry", uselist=False)
    raw_material = relationship("RawMaterial", back_populates="enquiry", uselist=False)
    process_tasks = relationship("ProcessTask", back_populates="enquiry")

class Designer(Base):
    __tablename__ = "designers"
    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, ForeignKey('enquiries.id'))
    design_file = Column(String)

    enquiry = relationship("Enquiry", back_populates="designer")

class OrderConfirmation(Base):
    __tablename__ = "order_confirmations"
    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, ForeignKey('enquiries.id'))
    po_number = Column(String)
    order_id = Column(String)

    enquiry = relationship("Enquiry", back_populates="order_confirmation")

class RawMaterial(Base):
    __tablename__ = "raw_materials"
    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, ForeignKey('enquiries.id'))
    material_available = Column(String)  # "Yes" or "No"

    enquiry = relationship("Enquiry", back_populates="raw_material")

class ProcessTask(Base):
    __tablename__ = "process_tasks"
    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, ForeignKey('enquiries.id'))
    quantity_given = Column(Integer)
    quantity_returned = Column(Integer)
    quantity_destroyed = Column(Integer)

    enquiry = relationship("Enquiry", back_populates="process_tasks")