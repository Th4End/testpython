from fastapi import FastAPI
from app.controller.discount_controller import router as discount_router
from app.controller.product_controller import router as product_router

app = FastAPI()

app.include_router(discount_router, prefix="/api/discount")
app.include_router(product_router, prefix="/api/products")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)