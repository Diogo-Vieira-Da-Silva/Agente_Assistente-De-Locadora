from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pydantic import BaseModel, Field

app = FastAPI(
    title="Minha Primeira API"
)


class Mensagem(BaseModel):
    texto: str = Field(min_length=1)

class Mensagem(BaseModel):
    texto: str


@app.post("/mensagem")
def receber_mensagem(mensagem: Mensagem):
    return {
        "mensagem_recebida": mensagem.texto
    }



@app.get("/", response_class=HTMLResponse)
def pagina_inicial():
    return """
    <h1>API em execução</h1>
    <p> FIAP - Let's rock the future!</p>
    """





@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}