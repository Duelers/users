from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String
)

meta = MetaData()

users = Table(
    'users', meta,

    Column('id', Integer, primary_key=True),
    Column('username', String(200), nullable=False),
    Column('password', String(512), nullable=False),
)