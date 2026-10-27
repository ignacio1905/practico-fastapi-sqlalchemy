from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

# Crea las tablas en la base sqlite si todavía no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Biblioteca", description="CRUD de libros con SQLAlchemy + SQLite")


@app.get("/")
def root():
    return {"mensaje": "API Biblioteca funcionando. Documentación en /docs"}


# ---------- CREATE ----------
@app.post("/libros", response_model=schemas.LibroOut, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    nuevo = models.Libro(**libro.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ---------- READ (lista) ----------
@app.get("/libros", response_model=list[schemas.LibroOut])
def listar_libros(
    leido: bool | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    consulta = select(models.Libro)
    if leido is not None:
        consulta = consulta.where(models.Libro.leido == leido)
    consulta = consulta.offset(skip).limit(limit)
    return db.scalars(consulta).all()


# ---------- READ (uno) ----------
@app.get("/libros/{libro_id}", response_model=schemas.LibroOut)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.get(models.Libro, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


# ---------- UPDATE (completo) ----------
@app.put("/libros/{libro_id}", response_model=schemas.LibroOut)
def reemplazar_libro(libro_id: int, datos: schemas.LibroCreate, db: Session = Depends(get_db)):
    libro = db.get(models.Libro, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    for campo, valor in datos.model_dump().items():
        setattr(libro, campo, valor)
    db.commit()
    db.refresh(libro)
    return libro


# ---------- UPDATE (parcial) ----------
@app.patch("/libros/{libro_id}", response_model=schemas.LibroOut)
def actualizar_libro(libro_id: int, datos: schemas.LibroUpdate, db: Session = Depends(get_db)):
    libro = db.get(models.Libro, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(libro, campo, valor)
    db.commit()
    db.refresh(libro)
    return libro


# ---------- DELETE ----------
@app.delete("/libros/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = db.get(models.Libro, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    db.delete(libro)
    db.commit()
