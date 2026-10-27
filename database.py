from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./biblioteca.db"

# check_same_thread=False es necesario en SQLite porque FastAPI
# puede atender una misma conexión desde distintos hilos.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Clase base de la que heredan todos los modelos."""


def get_db():
    """Dependencia de FastAPI: abre una sesión por request y la cierra al terminar."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
