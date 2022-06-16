from typing import Optional

from pydantic import BaseModel


# Input VIN Requested (string, exactly 17 alphanumeric characters)
# Make (String)
# Model (String)
# Model Year (String)
# Body Class (String)
# Cached Result? (Boolean)

# Shared properties
class VinBase(BaseModel):
    vin: str
    make: str
    model: str
    model_year: str
    body_class: str


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