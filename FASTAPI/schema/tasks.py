from pydantic import BaseModel,model_validator


# class Task(BaseModel):
#     price: str
#     sender: str
#     inn: str
#     pc: str
#     platej: str
#     data_plateja: str
#     naznach: str
#     _processing_timestamp: str

#     @model_validator(mode='after')
#     def check_for_nones(self):
#         if self.price is None or self.sender is None or self.inn is None or self.pc is None or self.platej is None :
#             raise ValueError('e,pty')
#         return self

class Task_FA(BaseModel):
    id: int
    price: int
    time: str
    
    class Config:
        from_attributes = True  # Добавьте это!

    @model_validator(mode='after')
    def check_for_nones(self):
        if self.id is None or self.price is None or self.time is None :
            raise ValueError('empty')
        return self