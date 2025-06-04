from fastapi import APIRouter, HTTPException
from typing import List
from app.model.ProductModel import Product
from app.service.ProductService import ProductService
from app.schemas.product_schema import ProductSchema


router = APIRouter(tags=["products"])
product_service = ProductService()

@router.get("/", response_model=List[ProductSchema])
def get_all_products():
    return product_service.get_all_products()

@router.get("/{id}", response_model=ProductSchema)
def get_product_by_id(id: int):
    product = product_service.get_product_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return product