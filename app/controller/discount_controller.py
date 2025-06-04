from app.service.discount_service import DiscountService
from fastapi import Query, APIRouter

router = APIRouter(prefix="/api/discounts", tags=["products"])
discount_service = DiscountService()

@router.get("/discount")
def get_discount(price: float = Query(..., gt=0)):
    discount = discount_service.calculate_discount(price)
    return {"price": price, "discount": discount}