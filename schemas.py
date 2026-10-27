from pydantic import BaseModel, ConfigDict, Field


class LibroBase(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    autor: str = Field(min_length=1, max_length=100)
    anio: int | None = Field(default=None, ge=0, le=2100)
    genero: str | None = Field(default=None, max_length=50)
    leido: bool = False


class LibroCreate(LibroBase):
    pass


class LibroUpdate(BaseModel):
    """Todos los campos opcionales, para PATCH (actualización parcial)."""

    titulo: str | None = Field(default=None, min_length=1, max_length=200)
    autor: str | None = Field(default=None, min_length=1, max_length=100)
    anio: int | None = Field(default=None, ge=0, le=2100)
    genero: str | None = Field(default=None, max_length=50)
    leido: bool | None = None


class LibroOut(LibroBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
