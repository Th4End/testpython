import pytest
from app.service.discount_service import DiscountService

discount_service = DiscountService()

def test_should_return_zero_discount_for_low_price():
    price = 50
    discount = discount_service.calculate_discount(price)
    assert discount == pytest.approx(0.0, rel=1e-4), "Le prix est inférieur à 100€, donc la remise doit être 0€"

def test_should_apply_ten_percent_discount():
    price = 150
    discount = discount_service.calculate_discount(price)
    assert discount == pytest.approx(15.0, rel=1e-4), "10% de 150€ doit donner une remise de 15€"
