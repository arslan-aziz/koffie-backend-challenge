from sqlalchemy import create_engine, MetaData, Table, String, Column
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# engine = create_engine('sqlite:///cache.db', pool_pre_ping=True)
engine = create_engine(
    "sqlite://",
    echo=True,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
metadata = MetaData()
# if not engine.has_table('vin'):  # If table don't exist, Create.
# metadata = MetaData(engine)
# Create a table with the appropriate Columns
Table(
    "vin",
    metadata,
    Column("vin", String, primary_key=True),
    Column("make", String, nullable=True),
    Column("model", String, nullable=True),
    Column("model_year", String, nullable=True),
    Column("body_class", String, nullable=True),
)
metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
