from contextlib import asynccontextmanager

from fastapi import status
from fastapi.responses import JSONResponse # para usar o lifespan startar e down
from controllers import conta, transacao, autenticacao # para definir eles no router
from fastapi import FastAPI, Request
from exceptions import AccountNotFoundError, BusinessError

from database import engine, Base, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    try:
        yield
    finally:
        await engine.dispose()
            
tags_metadata = [
    {
        'name' : 'Autenticação',
        'description': 'Rotas reponsáveis por cadastro e login de usuários.'
    },  
    {
        'name' : 'Contas',
        'description': 'Gerenciamento das contas bancárias do usuário.'
    },
    {
        'name' : 'Transações',
        'description': 'Operações financeiras como saques e depósitos.'
    }
]
            
app = FastAPI(title='API Bank System',
    version='1.0.0',
    openapi_tags=tags_metadata,
    description="""Sistema desenvolvido com FastAPI
    
    RECURSOS PRINCIPAIS
    - AUTENTICAÇÃO JWT
    - CADASTRO DE USUÁRIOS
    - CRIAÇÃO DE CONTAS
    - REGISTRO DE TRANSAÇÕES
    PROTEÇÃO DE ROTAS POR USUÁRIO AUTENTICADO.""",
    lifespan=lifespan,
    contact={
        'name': 'Itallo Polito',
        'email': 'itallomp@hotmail.com'
    })

        
    
app.include_router(conta.router, tags=['Contas'])
app.include_router(transacao.router, tags=['Transações'])
app.include_router(autenticacao.router, tags=['Autenticação'])

@app.exception_handler(AccountNotFoundError)
async def conta_nao_encontrada(request: Request, exc: AccountNotFoundError):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Conta não encontrada."})


@app.exception_handler(BusinessError)
async def business_error(request: Request, exc: BusinessError):
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)})