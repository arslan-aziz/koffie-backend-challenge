from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app import schemas, crud, service
from app.schemas.vin import VinDeleteResponse
from app.api import deps

router = APIRouter()


@router.get("/{vin}", response_model=schemas.VinDeleteResponse)
def remove(vin: str, db: Session = Depends(deps.get_db)):
    if not service.validate_vin(vin):
        raise HTTPException(
            400, detail="Invalid VIN. VIN must be 17 alphanumeric characters."
        )

    vin_orm_obj = crud.vin.get(db, vin)
    if vin_orm_obj:
        crud.vin.remove(db, vin)
        resp_data = {"vin": vin, "cache_delete_success": True}
    else:
        resp_data = {"vin": vin, "cache_delete_success": False}
    resp_obj = VinDeleteResponse.parse_obj(resp_data)
    return resp_obj
