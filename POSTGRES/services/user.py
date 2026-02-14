import string

from dataclasses import dataclass
from FASTAPI.schema.user import UserSchemaModel
from POSTGRES.repository.user import UserRepository

from random import choice


@dataclass
class UserService:
    user_repository: UserRepository
    def create_user(self, username:str, password:str) -> UserSchemaModel:
        acces_tocken = self._generate_access_tocken()
        user = self.user_repository.create_user(username=username,password=password,access_tocken=acces_tocken)
        return UserSchemaModel(user_id=user.id,access_tocken=user.access_tocken)
    
    @staticmethod
    def _generate_access_tocken() -> str:
        return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(12))