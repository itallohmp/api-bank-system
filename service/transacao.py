from schemas.transacao import TransacaoIn
from views.transacao import TransacaoOut
from sqlalchemy.ext.asyncio import AsyncSession
from models.transacao import TransacaoDB
from models.contas import ContaDB
from sqlalchemy.future import select
from schemas.transacao import TipoTransacao  #ENUM
from exceptions import *
from decimal import Decimal

class ServicosTransacoes:
    async def registrar_transacao(self, db: AsyncSession, conta_id: int, valor: float, tipo: TipoTransacao) -> TransacaoOut:
        conta = await db.get(ContaDB, conta_id)
        valor = Decimal(valor)
        
        if valor <= 0:
            raise BusinessError('Valor da transação deve ser maior que zero')
        
        if not conta:
            raise AccountNotFoundError('Conta não encontrada!')
        
        if tipo == 'saque':
                if conta.saldo < valor:
                    raise BusinessError('Saldo insuficiente')
                conta.saldo -= valor
                
        elif tipo == 'deposito':
            conta.saldo += valor
        else:
            raise BusinessError('Tipo de transação inválida')  
        
        transacao = TransacaoDB(conta_id=conta_id, valor=valor, tipo=tipo)
        

        db.add(transacao)
        await db.commit()
        await db.refresh(transacao)
        await db.refresh(conta)
            
        return TransacaoOut.model_validate(transacao, from_attributes=True)
    
    async def listar_transacao(self, db: AsyncSession, conta_id: int, limit:50, skip: int=0) -> list[TransacaoOut]:
        q = select(TransacaoDB).where(TransacaoDB.conta_id == conta_id).order_by(TransacaoDB.data.desc()).limit(limit).offset(skip)
        resultado = await db.execute(q)
        transacoes = resultado.scalars().all()
        
        return [TransacaoOut.model_validate(t, from_attributes=True) for t in transacoes]