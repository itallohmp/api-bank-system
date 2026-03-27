from schemas.contas import ContaIn
from views.contas import ContaOut
from models.contas import ContaDB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class ServicosConta:
    async def criar_conta(self, db: AsyncSession, conta_in: ContaIn, usuario_id: int) -> ContaOut:
        dados = conta_in.model_dump()
        conta_db = ContaDB(nome=dados['nome'], usuario_id=usuario_id)
        db.add(conta_db)
        await db.commit()
        await db.refresh(conta_db)
        return ContaOut.model_validate(conta_db, from_attributes=True)
    
    
    async def listar_contas(self, db: AsyncSession, limit: int, skip: int =0) -> list[ContaOut]:
        q = select(ContaDB).limit(limit).offset(skip)
        resultado = await db.execute(q)
        contas = resultado.scalars().all()
        return[ContaOut.model_validate(c, from_attributes=True) for c in contas]