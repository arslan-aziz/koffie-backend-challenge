from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, service
from app.service.vpic_api import VpicApi
from app.api import deps


router = APIRouter()


@router.get("/{vin}", response_model=schemas.VinCreateResponse)
def lookup(
    vin: str,
    db: Session = Depends(deps.get_db),
    vpic_api: VpicApi = Depends(deps.get_vpic_api),
):
    if not service.validate_vin(vin):
        raise HTTPException(
            400, detail="Invalid VIN. VIN must be 17 alphanumeric characters."
        )

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
