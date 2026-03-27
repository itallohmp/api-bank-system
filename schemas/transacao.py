from pydantic import BaseModel, PositiveFloat
from enum import Enum
from decimal import Decimal

class TipoTransacao(Enum):
    DEPOSITO = 'deposito'
    SAQUE = 'saque'
    

class TransacaoIn(BaseModel):
    conta_id: int
    valor: Decimal
    tipo: TipoTransacao
    
    class Config:
        use_enum_values = True