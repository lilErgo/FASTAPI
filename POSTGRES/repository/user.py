from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from dataclasses import dataclass

from POSTGRES.models.user import UserProfile

@dataclass
class UserRepository:
    db_session: Session

    def create_user(self, username:str, password:str, access_tocken:str) -> UserProfile:
        query = insert(UserProfile).values(username=username,password=password,access_tocken=access_tocken).returning(UserProfile.id)
        with self.db_session() as session:
            user_id:int = session.execute(query).scalar_one_or_none()
            session.commit()
            # session.flush()
            return self.get_user(user_id)
        
    def get_user(self, user_id) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.id == user_id)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()
            