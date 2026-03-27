from pydantic import BaseModel, PositiveFloat
from datetime import datetime

class ContaOut(BaseModel):
    id: int
    nome: str
    saldo: float
    data_criacao: datetime
    

class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    tipo: str
    valor: PositiveFloat
    data_criacao: datetime