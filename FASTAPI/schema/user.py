from pydantic import BaseModel, model_validator

class UserSchemaModel(BaseModel):
    user_id: int
    access_tocken: str
    @model_validator(mode='after')
    def check_for_nones(self):
        if  self.user_id is None or self.access_tocken is None or \
            not isinstance(self.user_id, int) or not isinstance(self.access_tocken, str):
            raise ValueError('Empty or inccorect')
        return self

class UserSchemaModelDoCreate(BaseModel):
    username:str
    password:str

    @model_validator(mode='after')
    def check_for_nones(self):
        if  (self.username is None or self.password is None) or \
            (not isinstance(self.username, str) or not isinstance(self.password, str)) or \
            (self.username == '' or self.password == '') or \
            (self.username.startswith(' ') or self.password.startswith(' ')):

            raise ValueError('Empty or inccorect')
        return self
    


    # if self.username is None or self.password is None or isinstance(self.username,str) is False or isinstance(self.password,str) is False or \
    #     self.username == '' or self.password == '' or self.username.startswith(' ') or self.password.startswith(' ') 