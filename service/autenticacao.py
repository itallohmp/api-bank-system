from fastapi import HTTPException

from schemas.autenticacao import UsuarioIn
from views.autenticacao import UsuarioOut
from views.autenticacao import TokenOut
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.usuarios import Usuario
from security import *
from exceptions import *

class ServicoLogin:
    async def logar(self, db: AsyncSession, usuario_in: UsuarioIn) -> TokenOut:
        q = select(Usuario).where(Usuario.login == usuario_in.login)
        resultado = await db.execute(q)
        usuario = resultado.scalar_one_or_none()
        
        if not usuario:
            raise HTTPException(status_code=401, detail="Login ou senha inválidos")

        if not verificar_senha(usuario_in.senha, usuario.senha):
            raise HTTPException(status_code=401, detail="Login ou senha inválidos")

        token = criar_token(usuario.id)

        return TokenOut(access_token=token,token_type="bearer")       
        
    async def registrar(self, db: AsyncSession, usuario_in: UsuarioIn) -> UsuarioOut:
        q = select(Usuario).where(Usuario.login == usuario_in.login)
        resultado = await db.execute(q)
        usuario = resultado.scalar_one_or_none()
        
        print(usuario_in.senha)
        print(type(usuario_in.senha))
        print(len(usuario_in.senha))
        
        if usuario:
            raise BusinessError('Ja existe um login com este nome.')
        
        usuario_db = Usuario(login=usuario_in.login, senha=hash_senha(usuario_in.senha))
        
        db.add(usuario_db)
        await db.commit()
        await db.refresh(usuario_db)
        
        return UsuarioOut.model_validate(usuario_db, from_attributes=True)
        