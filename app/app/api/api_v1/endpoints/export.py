from app.service.vpic_api import VpicApi
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
import pandas as pd

from app.api import deps
from app import schemas, crud, service
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_class=FileResponse)
def export(
    db: Session = Depends(deps.get_db)):

    df = pd.read_sql('SELECT * FROM vin', db.bind)
    df.to_parquet('vin.parquet', index = False)
    return 'vin.parquet'