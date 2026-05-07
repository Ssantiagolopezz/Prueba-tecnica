from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root@localhost/logistica_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Orden(Base):
    __tablename__ = "ordenes"

    id = Column(Integer, primary_key=True, index=True)
    proveedor = Column(String(100))
    producto = Column(String(100))
    cantidad = Column(Integer)
    fecha_entrega = Column(Date)
    prioridad = Column(String(20))
    estado = Column(String(50), default="Pendiente")


def init_db():
    Base.metadata.create_all(bind=engine)