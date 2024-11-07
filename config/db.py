from typing import Annotated

from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends


sqlite_file_name = "basededatos.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables(tables_order):
    SQLModel.metadata.create_all(engine, tables=tables_order)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]