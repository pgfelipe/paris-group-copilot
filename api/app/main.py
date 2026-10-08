from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models
from app.db import Base, engine, get_db
from app.schemas import HipoteseIn, HipoteseOut, ProjetoIn, ProjetoOut

# MVP: tabelas criadas no boot. Migrations versionadas (Alembic) ficam para depois.
Base.metadata.create_all(engine)

app = FastAPI(
    title="Paris Group Copilot API",
    description="Conhecimento de MVPs passados: projetos e as hipóteses testadas em cada um.",
    version="0.1.0",
)


@app.get("/projetos", response_model=list[ProjetoOut], tags=["Projeto"])
def listar_projetos(db: Session = Depends(get_db)):
    return db.scalars(select(models.Projeto)).all()


@app.post("/projetos", response_model=ProjetoOut, status_code=201, tags=["Projeto"])
def criar_projeto(payload: ProjetoIn, db: Session = Depends(get_db)):
    projeto = models.Projeto(**payload.model_dump())
    db.add(projeto)
    db.commit()
    db.refresh(projeto)
    return projeto


@app.get("/hipoteses", response_model=list[HipoteseOut], tags=["Hipótese"])
def listar_hipoteses(projeto_id: int | None = None, db: Session = Depends(get_db)):
    query = select(models.Hipotese)
    if projeto_id is not None:
        query = query.where(models.Hipotese.projeto_id == projeto_id)
    return db.scalars(query).all()


@app.post("/hipoteses", response_model=HipoteseOut, status_code=201, tags=["Hipótese"])
def criar_hipotese(payload: HipoteseIn, db: Session = Depends(get_db)):
    if db.get(models.Projeto, payload.projeto_id) is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    hipotese = models.Hipotese(**payload.model_dump())
    db.add(hipotese)
    db.commit()
    db.refresh(hipotese)
    return hipotese
