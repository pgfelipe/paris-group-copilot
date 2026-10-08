from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

StatusProjeto = Literal["discovery", "mvp", "validado", "encerrado"]
ResultadoHipotese = Literal["em_teste", "validada", "refutada"]


class ProjetoIn(BaseModel):
    nome: str = Field(examples=["Agenda IA para clínicas"])
    problema: str = Field(examples=["Clínicas perdem 20% dos horários por falta"])
    publico: str = Field(examples=["Recepcionistas de clínicas pequenas"])
    status: StatusProjeto = "discovery"
    aprendizado: str | None = Field(
        default=None, examples=["Lembrete por WhatsApp funcionou, e-mail não"]
    )


class ProjetoOut(ProjetoIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


class HipoteseIn(BaseModel):
    projeto_id: int
    se: str = Field(examples=["Se enviarmos lembrete automático por WhatsApp"])
    entao: str = Field(examples=["então a clínica reduzirá faltas"])
    porque: str = Field(examples=["porque o paciente lê WhatsApp mais do que e-mail"])
    metrica: str = Field(examples=["Faltas caem de 20% para 10% em 4 semanas"])
    resultado: ResultadoHipotese = "em_teste"
    evidencia: str | None = Field(
        default=None, examples=["Caiu para 12%; 3 de 4 clínicas bateram a meta"]
    )


class HipoteseOut(HipoteseIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
