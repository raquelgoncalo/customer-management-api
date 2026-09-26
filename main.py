from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.customers import router as customers_router


app = FastAPI(
    title="Customer Management API",
    description="API REST para gerenciamento de clientes.",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(customers_router)


@app.get("/", tags=["Health"])
def home():
    return {
        "message": "Customer Management API",
        "status": "online",
    }