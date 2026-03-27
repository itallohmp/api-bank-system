from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

Base = declarative_base()

DATABASE_URL = settings.database_url # importado do config


engine = create_async_engine(DATABASE_URL, echo=True, future=True) #echo mostra log do sql
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False,)

async def get_db():
    async with AsyncSessionLocal() as session:  # função que garante o fechamen to das seções
        yield session