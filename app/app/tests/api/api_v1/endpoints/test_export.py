from fastapi.testclient import TestClient
import pytest
import pandas as pd
import io

from app.main import app

client = TestClient(app)


@pytest.fixture()
def test_vins():
    return [
        "1XPWD40X1ED215307",
        "1XKWDB0X57J211825",
        "1XP5DB9X7YN526158",
        "4V4NC9EJXEN171694",
    ]


# test that cache export contains all cached vins
def test_cache_export(test_vins):
    # have server cache vins
    for vin in test_vins:
        response = client.get(f"/api/v1/lookup/{vin}")
        assert response.status_code == 200

    response = client.get("/api/v1/export")
    pq_file = io.BytesIO(response.content)
    found_vins = pd.read_parquet(pq_file).vin.tolist()

    assert len(set(test_vins).symmetric_difference(set(found_vins))) == 0
