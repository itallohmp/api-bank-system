from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class ContaDB(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    saldo = Column(Numeric(12, 2), default=0)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='contas')
    transacoes = relationship('TransacaoDB', back_populates='conta')