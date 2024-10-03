from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()


blog = Table(
    "blog",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("news", String, nullable=False),
    Column("created", TIMESTAMP, default=datetime.utcnow),
)