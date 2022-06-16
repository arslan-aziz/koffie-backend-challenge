from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.vin import VinOrm
from app.schemas.vin import VinCreate


class CRUDVin:
    def __init__(self):
        pass

    def get(self, db: Session, vin: str) -> Optional[VinOrm]:
        return db.query(VinOrm).filter(VinOrm.vin == vin).first()

    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[VinOrm]:
        return db.query(VinOrm).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: VinCreate) -> VinOrm:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = VinOrm(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(
    #     self,
    #     db: Session,
    #     db_obj: VinOrm,
    #     obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    # ) -> ModelType:
    #     obj_data = jsonable_encoder(db_obj)
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         if field in update_data:
    #             setattr(db_obj, field, update_data[field])
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def remove(self, db: Session, id: int) -> VinOrm:
        obj = db.query(VinOrm).get(id)
        db.delete(obj)
        db.commit()
        return obj

vin = CRUDVin()