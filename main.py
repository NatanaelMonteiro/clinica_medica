from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()
app.mount("/app", StaticFiles(directory="static", html="true"), name="static")


@app.get("/", response_class=RedirectResponse)
async def root():
    return "/app/login.html"


@app.get("/api", response_class=RedirectResponse)
async def api():
    return "/app/login.html"


@app.get("/api/pacientes")
async def pacientes():
    return get_pacientes()


@app.get("/api/medicos")
async def medicos(request: Request):
    medicos = get_medicos()
    return medicos


# @app.get("/api/medicos", response_class=HTMLResponse)
# async def medicos():
#     dados_html = """
#         <table>
#             <thead>
#                 <tr>
#                     <th>Nome</th>
#                     <th>RCM</th>
#                     <th>Especialidade</th>
#                     <th>Turno</th>
#                     <th>Situação</th>
#                     <th colspam="2">&nbsp;</th>
#                 </tr>
#             </thead>
#             <tbody>
#                 <tr>
#                     <td>Rancho Crux</td>
#                     <td>0001</td>
#                     <td>Traumatologia</td>
#                     <td>Noturno</td>
#                     <td>Ativo</td>
#                     <td>
#                         <i class="fa fa-pencil"></i>&nbsp;
#                     </td>
#                     <td>
#                         <i class="fa fa-trash-o"></i>
#                     </td>
#                 </tr>
#             </tbody>
#         </table>
#         """

#     return dados_html


def get_medicos():
    dados = [
        {
            "nome": "Rancho Crux",
            "crm": "0001",
            "especialidade": "Traumatologia",
            "turno": "Noturno",
            "situação": "Ativo",
        },
        {
            "nome": "Álvaro Cortez",
            "crm": "0002",
            "especialidade": "Radiologia",
            "turno": "Vespertino",
            "situação": "Ativo",
        },
    ]

    return dados


def get_pacientes():
    dados = [
        {
            "nome": "Natanael Lima",
            "email": "natan@gmail.com",
            "telefone": "61 9999-0000",
            "situação": "internado",
        },
        {
            "nome": "Luciana Lima",
            "email": "lulu@gmail.com",
            "telefone": "61 9999-2222",
            "situação": "em atendimento",
        },
    ]

    return dados
