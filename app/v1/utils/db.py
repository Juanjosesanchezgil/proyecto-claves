import peewee
from contextvars import ContextVar
from fastapi import Depends

from app.v1.utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None }
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)