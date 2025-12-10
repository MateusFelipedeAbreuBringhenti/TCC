from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, JSON, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

DATABASE_URL = "postgresql+psycopg2://Mateus:123456@localhost:5432/TCCBanco"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    nome_arquivo = Column(String, nullable=False)
    binario = Column(LargeBinary, nullable=False)
    tst = Column(JSON, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)
