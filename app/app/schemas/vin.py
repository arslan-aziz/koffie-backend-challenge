from typing import Optional

from pydantic import BaseModel

# Shared properties
class VinBase(BaseModel):
    vin: str
    make: Optional[str] = ""
    model: Optional[str] = ""
    model_year: Optional[str] = ""
    body_class: Optional[str] = ""


# Properties to create Vin in db
class VinCreate(VinBase):
    pass


# Properties to return to client
class VinCreateResponse(VinBase):
    cached_result: bool = False

    class Config:
        orm_mode = True


class VinDeleteResponse(BaseModel):
    vin: str
    cache_delete_success: bool
