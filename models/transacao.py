from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class TransacaoDB(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True, index=True)
    conta_id = Column(Integer, ForeignKey('contas.id', ondelete='CASCADE'), nullable=False)
    tipo = Column(String, nullable=False)
    valor = Column(Numeric(12, 2), nullable=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    conta = relationship('ContaDB', back_populates='transacoes')