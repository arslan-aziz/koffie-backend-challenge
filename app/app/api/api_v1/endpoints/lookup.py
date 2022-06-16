from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.service.vpic_api import VpicApi


router = APIRouter()

@router.get("/{vin}", response_model=schemas.VinCreateResponse)
def lookup(
    vin: str,
    db: Session = Depends(deps.get_db),
    vpic_api: VpicApi = Depends(deps.get_vpic_api)):
    # TODO validation

    vin_orm_obj = crud.vin.get(db, vin)
    if vin_orm_obj:
        resp_obj = schemas.VinCreateResponse.from_orm(vin_orm_obj)
        resp_obj.cached_result = True
        return resp_obj
    if vin_orm_obj is None:
        # otherwise contact vPIC API to decode vin, store result, return
        vpic_create_obj = vpic_api.decode_vin(vin)
        vin_orm_obj = crud.vin.create(db, vpic_create_obj)
        resp_obj = schemas.VinCreateResponse.from_orm(vin_orm_obj)
        resp_obj.cached_result = False
        return resp_obj
