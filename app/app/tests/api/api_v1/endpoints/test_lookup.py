from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)


@pytest.fixture()
def test_vin():
    return "1XPWD40X1ED215307"


# test a VIN with invalid format
def test_read_item_invalid():
    INVALID_VIN = "abc123"
    response = client.get(f"/api/v1/lookup/{INVALID_VIN}")
    assert response.status_code == 400


# test a vin with with valid format
def test_read_item_valid(test_vin):
    response = client.get(f"/api/v1/lookup/{test_vin}")
    assert response.status_code == 200
    data = response.json()
    assert data["make"] == "PETERBILT"
    assert data["model"] == "388"
    assert data["model_year"] == "2014"
    assert data["body_class"] == "Truck-Tractor"


# test a vin that was cached in the previous test
def test_read_item_cached(test_vin):
    response = client.get(f"/api/v1/lookup/{test_vin}")
    assert response.status_code == 200
    data = response.json()
    assert data["cached_result"] == True
