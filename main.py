from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/app", StaticFiles(directory="static", html="true"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=RedirectResponse)
async def root():
    return "/app/login.html"


@app.get("/api", response_class=RedirectResponse)
async def api():
    return "/app/login.html"


@app.get("/api/medicos", response_class=HTMLResponse)
async def medicos(request: Request):
    medicos = get_medicos()
    dados_html= templates.TemplateResponse("tpl_medicos.html", {"request": request, "dados": medicos})
                                           
    return dados_html


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
