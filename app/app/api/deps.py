from this import d
from typing import Generator

from app.db.session import SessionLocal
from app.service.vpic_api import VpicApi
from app.core.config import VPIC_API_URL

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_vpic_api() -> Generator:
    try:
        vpic_api = VpicApi(VPIC_API_URL)
        yield vpic_api
    finally:
        pass