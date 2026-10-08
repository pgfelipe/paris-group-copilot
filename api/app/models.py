from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Projeto(Base):
    __tablename__ = "projetos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(200))
    problema: Mapped[str] = mapped_column(Text)
    publico: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20))
    aprendizado: Mapped[str | None] = mapped_column(Text)

    hipoteses: Mapped[list["Hipotese"]] = relationship(back_populates="projeto")


class Hipotese(Base):
    __tablename__ = "hipoteses"

    id: Mapped[int] = mapped_column(primary_key=True)
    projeto_id: Mapped[int] = mapped_column(ForeignKey("projetos.id"))
    se: Mapped[str] = mapped_column(Text)
    entao: Mapped[str] = mapped_column(Text)
    porque: Mapped[str] = mapped_column(Text)
    metrica: Mapped[str] = mapped_column(Text)
    resultado: Mapped[str] = mapped_column(String(20))
    evidencia: Mapped[str | None] = mapped_column(Text)

    projeto: Mapped[Projeto] = relationship(back_populates="hipoteses")
