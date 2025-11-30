from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import Usuario

app = FastAPI(title="Microservicio de Usuarios (SQL)", version="1.0.0")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@app.get("/usuarios/", response_model=list[Usuario])
def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios

@app.get("/")
def home():
    return {"mensaje": "Microservicio de Usuarios corriendo en puerto 8001"}