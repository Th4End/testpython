class DiscountService:
    def calculate_discount(self, price: float) -> float:
        if price > 100:
            return price * 0.10
        return 0.0