from fastapi import APIRouter, Depends
from database import get_db

from views.transacao import TransacaoOut
from schemas.transacao import TransacaoIn
from sqlalchemy.ext.asyncio import AsyncSession
from service.transacao import ServicosTransacoes
from security import get_current_user

router = APIRouter(prefix='/transacoes', dependencies=[Depends(get_current_user)])

tx_servicos = ServicosTransacoes()

@router.post('/', response_model=TransacaoOut)
async def reg_transacao(transcao_in: TransacaoIn, db: AsyncSession = Depends(get_db)):
    return await tx_servicos.registrar_transacao(conta_id=transcao_in.conta_id, valor=transcao_in.valor, tipo=transcao_in.tipo, db=db)

