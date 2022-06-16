from sqlalchemy.orm import Session
import pandas as pd

from fastapi import APIRouter, Depends, Request
from fastapi.responses import FileResponse

from app.api import deps
from app.rate_limiter import limiter

router = APIRouter()


@router.get("/", response_class=FileResponse)
@limiter.limit("10/minute")
def export(request: Request, db: Session = Depends(deps.get_db)):
    df = pd.read_sql("SELECT * FROM vin", db.bind)
    df.to_parquet("vin.parquet", index=False)
    return "vin.parquet"
