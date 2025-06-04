import sys
import os
from tqdm import tqdm
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from fastapi.testclient import TestClient
from app.main import app
from app.model.ProductModel import Product

client = TestClient(app)

tests = []

def test_should_return_all_products(mocker):
    mock_service = mocker.patch("app.controller.product_controller.product_service")
    mock_service.get_all_products.return_value = [
        Product(id=1, name="Laptop", price=1200.0),
        Product(id=2, name="Smartphone", price=800.0)
    ]

    response = client.get("/api/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Laptop"
    assert data[1]["name"] == "Smartphone"

tests.append(test_should_return_all_products)

def test_should_return_product_by_id(mocker):
    mock_service = mocker.patch("app.controller.product_controller.product_service")
    mock_service.get_product_by_id.return_value = Product(id=1, name="Laptop", price=1200.0)

    response = client.get("/api/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

tests.append(test_should_return_product_by_id)

def test_should_return_404_for_unknown_id(mocker):
    mock_service = mocker.patch("app.controller.product_controller.product_service")
    mock_service.get_product_by_id.return_value = None

    response = client.get("/api/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produit non trouvé"

tests.append(test_should_return_404_for_unknown_id)

if __name__ == "__main__":
    from unittest.mock import MagicMock
    mocker = MagicMock()
    for test in tqdm(tests, desc="Tests en cours"):
        test(mocker)
