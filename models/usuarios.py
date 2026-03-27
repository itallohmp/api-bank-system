from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, String, Integer

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)

    contas = relationship('ContaDB', back_populates='usuario')