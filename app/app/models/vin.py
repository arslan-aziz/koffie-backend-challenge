from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class VinOrm(Base):

    __tablename__ = "vin"

    vin = Column(String, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    model_year = Column(String)
    body_class = Column(String)
