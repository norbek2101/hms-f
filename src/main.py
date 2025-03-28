from fastapi import FastAPI
from src.database import engine, Base
from src.auth.controller import router as auth_router

app = FastAPI()

# Initialize database
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Welcome to the HMS API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
