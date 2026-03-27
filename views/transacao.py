from pydantic import BaseModel, PositiveFloat
from datetime import datetime

class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    tipo: str
    valor: PositiveFloat
    data_criacao: datetime