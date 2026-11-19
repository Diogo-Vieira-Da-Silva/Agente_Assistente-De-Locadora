from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

from config import MODEL_NAME

carros = {
    "CAR-101": {
        "codigo": "CAR-101",
        "modelo": "Toyota Corolla",
        "categoria": "Sedan",
    },
    "CAR-202": {
        "codigo": "CAR-202",
        "modelo": "Jeep Renegade",
        "categoria": "SUV",
    },
}

alugueis = {
    "ALU-500": {
        "aluguel": "ALU-500",
        "status": "ativo",
        "codigo_carro": "CAR-101",
    },
    "ALU-501": {
        "aluguel": "ALU-501",
        "status": "ativo",
        "codigo_carro": "CAR-202",
    }
}


def consultar_carro(codigo: str) -> dict:
    """Consulta modelo e categoria de um carro pelo código."""
    codigo = codigo.strip().upper()

    if not codigo.startswith("CAR-"):
        return {"erro": "código de carro inválido"}

    carro = carros.get(codigo)

    if carro is None:
        return {"erro": "carro não encontrado"}

    return carro.copy()


def consultar_aluguel(aluguel: str) -> dict:
    """Consulta status e código do carro associado a um aluguel."""
    aluguel = aluguel.strip().upper()

    if not aluguel.startswith("ALU-"):
        return {"erro": "identificador de aluguel inválido"}

    registro = alugueis.get(aluguel)

    if registro is None:
        return {"erro": "aluguel não encontrado"}

    return registro.copy()


def estender_aluguel(aluguel: str) -> dict:
    """Estende o período de um aluguel ativo e devolve seu novo estado."""
    aluguel = aluguel.strip().upper()

    if not aluguel.startswith("ALU-"):
        return {"erro": "identificador de aluguel inválido"}

    registro = alugueis.get(aluguel)

    if registro is None:
        return {"erro": "aluguel não encontrado"}

    if registro["status"] != "ativo":
        return {
            "erro": "aluguel não pode ser estendido",
            "status_atual": registro["status"],
        }

    registro["status"] = "estendido"
    return registro.copy()


consultar_carro_tool = tool(consultar_carro)
consultar_aluguel_tool = tool(consultar_aluguel)
estender_aluguel_tool = tool(estender_aluguel)

tools_locadora = [
    consultar_carro_tool,
    consultar_aluguel_tool,
    estender_aluguel_tool,
]

SYSTEM_PROMPT = """
Você atende clientes de uma locadora de veículos.

- Use as tools para consultar carros e aluguéis.
- Não invente carros, aluguéis, códigos ou resultados.
- Se faltar um identificador necessário, peça esse dado.
- Para descobrir informações do carro associado a um aluguel,
  consulte primeiro o aluguel e use o codigo_carro retornado.
- Use estender_aluguel somente quando o usuário pedir explicitamente
  a extensão ou renovação do aluguel.
- Responda de forma objetiva depois de obter os dados necessários.
"""

model = init_chat_model(MODEL_NAME)
checkpointer = InMemorySaver()

agente_locadora = create_agent(
    model=model,
    tools=tools_locadora,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)


def responder(message: str, conversation_id: str) -> str:
    result = agente_locadora.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": conversation_id,
            }
        },
    )

    return result["messages"][-1].text