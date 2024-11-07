from sqlalchemy import Boolean,Column,Integer,String
from sqlalchemy.orm import declarative_base

from db import engine

Base=declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"  

    id_usuario = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    correo = Column(String(45), unique=True, nullable=False)
    contraseña = Column(String(45), nullable=False)

Base.metadata.create_all(engine)