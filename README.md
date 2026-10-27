# Práctico FastAPI 4: SQLAlchemy

API de biblioteca (CRUD de libros) con FastAPI, SQLAlchemy y SQLite.

## Estructura

- `database.py`: engine, `SessionLocal`, `Base` y la dependencia `get_db`
- `models.py`: modelo `Libro` (tabla `libros`)
- `schemas.py`: schemas de Pydantic (create, update, out)
- `main.py`: app FastAPI con los endpoints CRUD

## Cómo correrlo

```bash
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

La documentación interactiva queda en http://127.0.0.1:8000/docs
La base `biblioteca.db` se crea sola al arrancar.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/libros` | Crear un libro |
| GET | `/libros` | Listar (filtro opcional `?leido=true`, `skip`, `limit`) |
| GET | `/libros/{id}` | Obtener un libro |
| PUT | `/libros/{id}` | Reemplazar un libro |
| PATCH | `/libros/{id}` | Actualizar parcialmente |
| DELETE | `/libros/{id}` | Eliminar un libro |
