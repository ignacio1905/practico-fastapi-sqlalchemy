from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    autor: Mapped[str] = mapped_column(String(100), nullable=False)
    anio: Mapped[int | None] = mapped_column(Integer, nullable=True)
    genero: Mapped[str | None] = mapped_column(String(50), nullable=True)
    leido: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
