# backend/app/main.py

from fastapi import FastAPI
from app.routers.enquiry import router as enquiry_router
from app.routers.designer import router as designer_router
from app.routers.order import router as order_router
from app.routers.raw_material import router as raw_material_router
from app.routers.process import router as process_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Include routers
app.include_router(enquiry_router)
app.include_router(designer_router)
app.include_router(order_router)
app.include_router(raw_material_router)
app.include_router(process_router)