from dataclasses import dataclass
from FASTAPI.schema.user import UserSchemaModel

@dataclass
class Auth:
    def login(self, username:str, password:str) -> UserSchemaModel:
        pass