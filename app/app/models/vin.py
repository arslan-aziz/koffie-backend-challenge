from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class VinOrm(Base):

    __tablename__ = "vin"

    vin = Column(String, primary_key=True, index=True)
    make = Column(String, nullable=True)
    model = Column(String, nullable=True)
    model_year = Column(String, nullable=True)
    body_class = Column(String, nullable=True)
