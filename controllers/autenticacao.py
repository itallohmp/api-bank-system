from fastapi import APIRouter, Depends
from sqlalchemy import select

from schemas.autenticacao import UsuarioIn
from views.autenticacao import TokenOut
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from service.autenticacao import ServicoLogin
from views.autenticacao import UsuarioOut

auth = ServicoLogin()

router = APIRouter(prefix='/auth') 

@router.post('/login', response_model=TokenOut)
async def logar(dados: UsuarioIn, db: AsyncSession = Depends(get_db)):
    return await auth.logar(db, dados)

@router.post('/registrar', response_model=UsuarioOut)
async def registrar(dados: UsuarioIn, db: AsyncSession = Depends(get_db)):
    return await auth.registrar(db, dados)