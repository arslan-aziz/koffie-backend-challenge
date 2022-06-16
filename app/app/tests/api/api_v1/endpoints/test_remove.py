from fastapi.testclient import TestClient
import pytest

from app.main import app

client = TestClient(app)


@pytest.fixture()
def test_vin():
    return "1XPWD40X1ED215307"


# test removal of vin cached by server
def test_remove_cached_item(test_vin):
    # assume server caches vin (validate against test_lookup)
    response = client.get(f"/api/v1/lookup/{test_vin}")

    # remove the vin
    response = client.get(f"/api/v1/remove/{test_vin}")
    assert response.status_code == 200
    data = response.json()
    assert data["cache_delete_success"] == True


# test removal of vin not cached by server
def test_remove_uncached_item(test_vin):
    # remove the vin
    response = client.get(f"/api/v1/remove/{test_vin}")
    assert response.status_code == 200
    data = response.json()
    assert data["cache_delete_success"] == False
