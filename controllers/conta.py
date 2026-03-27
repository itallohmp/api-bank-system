from fastapi import APIRouter, Depends

from schemas.contas import ContaIn
from views.contas import *
from service.contas import ServicosConta
from service.transacao import ServicosTransacoes
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from security import get_current_user

router = APIRouter(prefix='/contas', dependencies=[Depends(get_current_user)]) 

servicos_contas = ServicosConta()
tx_servicos = ServicosTransacoes()


@router.post('/', response_model=ContaOut)
async def criar_conta(conta_in: ContaIn, db: AsyncSession = Depends(get_db), user_id = Depends(get_current_user)):
    return await servicos_contas.criar_conta(db=db, conta_in=conta_in, usuario_id=user_id)

@router.get('/', response_model=list[ContaOut])
async def listar_contas(limit: int=50, skip: int=0, db: AsyncSession = Depends(get_db)):
    return await servicos_contas.listar_contas(db=db, limit=limit, skip=skip)

@router.get('/{conta_id}/transactions', response_model=list[TransacaoOut])
async def listar_transacoes(conta_id: int, limit: int=50, skip: int=0, db: AsyncSession = Depends(get_db)):
    return await tx_servicos.listar_transacao(db=db, conta_id=conta_id, limit=limit, skip=skip)