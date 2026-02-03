from pydantic import BaseModel,model_validator


class Task(BaseModel):
    price: str
    sender: str
    inn: str
    pc: str
    platej: str
    data_plateja: str
    naznach: str
    _processing_timestamp: str

    @model_validator(mode='after')
    def check_for_nones(self):
        if self.price is None or self.sender is None or self.inn is None or self.pc is None or self.platej is None :
            raise ValueError('e,pty')
        return self