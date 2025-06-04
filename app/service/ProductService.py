from app.model.ProductModel import Product

class ProductService:
    def __init__(self):
        self.products = [
            Product(1, "Laptop", 1200.0),
            Product(2, "Smartphone", 800.0)
        ]
    def get_all_products(self):
        return self.products
    
    def get_product_by_id(self, product_id: int):
        return next((p for p in self.products if p.id == product_id), None)