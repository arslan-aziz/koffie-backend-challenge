from app.schemas.vin import VinDeleteResponse
from app.service.vpic_api import VpicApi
from fastapi import APIRouter, Depends

from app.api import deps
from app import schemas, crud, service
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{vin}", response_model=schemas.VinDeleteResponse)
def remove(
    vin: str,
    db: Session = Depends(deps.get_db)):
    # TODO validation

    vin_orm_obj = crud.vin.get(db, vin)
    if vin_orm_obj:
        crud.vin.remove(db, vin)
        resp_data = {
            'vin': vin,
            'cache_delete_success': True
        }
    else:
        resp_data = {
            'vin': vin,
            'cache_delete_success': False
        }
    resp_obj = VinDeleteResponse.parse_obj(resp_data)
    return resp_obj