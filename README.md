# Rental Assistant API

Design based on the Hands-on of Chapter 6 of PAP.

The application provides, via FastAPI, the rental agent originally running on a notebook. The agent maintains the three tools of the base material and uses 'conversation_id' in the HTTP contract, internally converted to the 'thread_id' used by the checkpointer.

## Structure

"'text
api_of_assistant_of_locator/
├── main.py
├── agent.py
├── schemas.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
"'

## 1. Create and activate the virtual environment

"'bash
python -m venv .venv
"'

macOS/Linux:

"'bash
source.venv/bin/activate
"'

Windows PowerShell:

"'powershell
.venv\Scripts\Activate.ps1
"'

## 2. Install the dependencies

"'bash
pip install -r requirements.txt
"'

## 3. Configure the key

Create '.env' from '.env.example':

"'text
GOOGLE_API_KEY=your_key_here
"'

The '.env' file is included in '.gitignore' and should not be pushed to GitHub.

## 4. Start the API

"'bash
fastapi dev main.py
"'

Interactive documentation will be available at:

"'text
http://127.0.0.1:8000/docs
"'

## 5. Test the API

### Health check

`GET /health`

Expected response:

"'json
{
  "status": "ok"
}
"'

### Chat

`POST /chat`

First round:

"'json
{
  "conversation_id": "car-001",
  "message": "I have the CAR-101 loan. What car is he associated with?
}
"'

Second round, keeping the same identifier:

"'json
{
  "conversation_id": "car-001",
  "message": "And what is his category?"
}
"'

The second response should use the context preserved in the conversation.

To validate isolation, repeat only the second question using another identifier:

"'json
{
  "conversation_id": "car-002",
  "message": "What type of car is it?"
}
"'

The new conversation should not inherit the context of 'car-001'.

## Available data

Cars:

- 'CAR-101' — code: CAR-101, model: Toyota Corolla, category: Sedan
- 'CAR-202' — code: CAR-202, model: Jeep Renegade, category: SUV

Rentals:

- 'ALU-500' - rental: ALU-500, status: active, Code_car: CAR-101,
- 'ALU-501' - rental: ALU-501, status: active, Code_car: CAR-202,

The agent can also explicitly extend the rental through the 'extend_rent' tool.

## Observation

'InMemorySaver' maintains state only while the application process is running. Restarting the server may erase the history of conversations.

--------------------------------------------------------------------TRADUÇÃO----------------------------------------------------------------------

# API do Assistente de Locadora

Projeto baseado no Hands-on do Capítulo 6 de PAP.

A aplicação disponibiliza, por FastAPI, o agente de locadora originalmente executado em notebook. O agente mantém as três tools do material-base e utiliza `conversation_id` no contrato HTTP, convertido internamente para o `thread_id` usado pelo checkpointer.

## Estrutura

```text
api_do_assistente_de_locadora/
├── main.py
├── agent.py
├── schemas.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 3. Configurar a chave

Crie `.env` a partir de `.env.example`:

```text
GOOGLE_API_KEY=sua_chave_aqui
```

O arquivo `.env` está incluído no `.gitignore` e não deve ser enviado ao GitHub.

## 4. Iniciar a API

```bash
fastapi dev main.py
```

A documentação interativa estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## 5. Testar a API

### Health check

`GET /health`

Resposta esperada:

```json
{
  "status": "ok"
}
```

### Chat

`POST /chat`

Primeiro turno:

```json
{
  "conversation_id": "carro-001",
  "message": "Tenho o empréstimo CAR-101. A qual carro ele está associado?"
}
```

Segundo turno, mantendo o mesmo identificador:

```json
{
  "conversation_id": "carro-001",
  "message": "E qual é a categoria dele?"
}
```

A segunda resposta deve utilizar o contexto preservado na conversa.

Para validar o isolamento, repita apenas a segunda pergunta usando outro identificador:

```json
{
  "conversation_id": "carro-002",
  "message": "Qual é o tipo do carro?"
}
```

A nova conversa não deve herdar o contexto de `carro-001`.

## Dados disponíveis

Carros:

- `CAR-101` — código: CAR-101, modelo: Toyota Corolla, categoria: Sedan
- `CAR-202` — código: CAR-202, modelo: Jeep Renegade, categoria: SUV

Aluguéis:

- `ALU-500` - aluguel: ALU-500, status: ativo, Codigo_carro: CAR-101,
- `ALU-501` - aluguel: ALU-501, status: ativo, Codigo_carro: CAR-202,

O agente também pode estender explicitamente o aluguel por meio da tool `estender_aluguel`.

## Observação

O `InMemorySaver` mantém o estado apenas enquanto o processo da aplicação está em execução. Reiniciar o servidor pode apagar o histórico das conversas.

--------------------------------------------------------------------Traducción--------------------------------------------------------------------

# API del asistente de alquiler

Diseño basado en la Práctica del Capítulo 6 del PAP.

La aplicación proporciona, a través de FastAPI, el agente de alquiler que originalmente se ejecutaba en una computadora portátil. El agente mantiene las tres herramientas del material base y utiliza 'conversation_id' en el contrato HTTP, convertido internamente al 'thread_id' utilizado por el checkpointer.

## Estructura

"'texto
api_del_asistente_del_localizador/
├── main.py
├── agente.py
├── esquemas.py
├── config.py
├── requisitos.txt
├── .env.ejemplo
├── .gitignore
└── README.md
"

## 1. Crear y activar el entorno virtual

"bash
python -m venv .venv
"

macOS/Linux:

"bash
fuente.venv/bin/activate
"

Windows PowerShell:

"'cáscara de poder
.venv\Scripts\Activate.ps1
"

## 2. Instalar las dependencias

"bash
pip install -r requisitos.txt
"

## 3. Configurar la clave

Crear '.env' a partir de '.env.example':

"'texto
GOOGLE_API_KEY=tu_clave_aquí
"

El archivo '.env' está incluido en '.gitignore' y no debe enviarse a GitHub.

## 4. Iniciar la API

"bash
fastapi dev main.py
"

La documentación interactiva estará disponible en:

"'texto
http://127.0.0.1:8000/docs
"

## 5. Pruebe la API

### Control de salud

`OBTENER /salud`

Respuesta esperada:

"json
{
  "estado": "ok"
}
"

### Charla

`POST /chat`

Primera ronda:

"json
{
  "conversation_id": "coche-001",
  "mensaje": "Tengo el préstamo CAR-101. ¿Con qué coche está asociado?
}
"

Segunda ronda, manteniendo el mismo identificador:

"json
{
  "conversation_id": "coche-001",
  "mensaje": "¿Y cuál es su categoría?"
}
"

La segunda respuesta debe utilizar el contexto preservado en la conversación.

Para validar el aislamiento, repita sólo la segunda pregunta utilizando otro identificador:

"json
{
  "conversation_id": "coche-002",
  "mensaje": "¿Qué tipo de coche es?"
}
"

La nueva conversación no debe heredar el contexto de 'car-001'.

## Datos disponibles

Coches:

- 'CAR-101' — código: CAR-101, modelo: Toyota Corolla, categoría: Sedán
- 'CAR-202' — código: CAR-202, modelo: Jeep Renegade, categoría: SUV

Alquileres:

- 'ALU-500' - alquiler: ALU-500, estado: activo, Code_car: CAR-101,
- 'ALU-501' - alquiler: ALU-501, estado: activo, Code_car: CAR-202,

El agente también puede extender explícitamente el alquiler a través de la herramienta 'extend_rent'.

## Observación

'InMemorySaver' mantiene el estado sólo mientras se ejecuta el proceso de aplicación. Reiniciar el servidor puede borrar el historial de conversaciones.

