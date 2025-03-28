from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import engine, Base
from src.api import router as api_router
from sqladmin import Admin
from src.auth.admin import UserAdmin
from src.hotels.admin import HotelAdmin

# Initialize database tables (if using raw SQLAlchemy without Alembic migrations)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Hotel Management System", version="1.0")

# Initialize SQLAdmin
admin = Admin(app, engine)

# CORS Middleware (Allow frontend access if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routers
app.include_router(api_router)


# Register the Admin Views
admin.add_view(UserAdmin)
admin.add_view(HotelAdmin)

# Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Hotel Management System API"}
