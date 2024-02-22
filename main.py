from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

import json
import time 
import urllib.parse as html

import db
import db_init
import static.fragments.html_edit as edit

app = FastAPI()
app.mount("/app", StaticFiles(directory="static", html="true"), name="static")

async def get_body(req: Request):
    payload = await req.body()
    payload = payload.decode("utf8")
    payload = html.unquote(payload)

    try:
        body = json.loads(payload)
    except:
        lista = list(payload.split("&"))
        body = dict(l.split("=") for l in lista)
    return body

@app.get("/", response_class=RedirectResponse)
async def root():
    return "/app/login.html"


@app.get("/api", response_class=RedirectResponse)
async def api():
    return "/app/login.html"


@app.get("/api/pacientes")
async def pacientes():
    dados = db.get_pacientes()
    time.sleep(2)
    return JSONResponse(dados)

@app.put("/api/pacientes/{id}", response_class=JSONResponse)
async def update_paciente(id, body=Depends(get_body)):
    db.update_paciente(id, body)
    dados = db.get_pacientes()
    return dados

@app.delete("/api/pacientes/{id}", response_class=HTMLResponse)
async def del_paciente(id: str):
    db.del_paciente(id)
    return ""

@app.get("/api/medicos", response_class=JSONResponse)
async def medicos():
    time.sleep(2)
    return db.get_medicos()

@app.delete("/api/medicos/{id}", response_class=HTMLResponse)
async def del_medico(id: str):
    db.del_medico(id)
    return ""

# RESETAR O BANDO DE DADOS
@app.get("/reset", response_class=RedirectResponse)
def db_reset():
    db_init.tables_init()
    return "/app/home.html"

# RETORNAR TEMPLATE PARA EDITAR PACIENTES
@app.get("/api/pacientes/{id}/edit", response_class=HTMLResponse)
async def edit_paciente(id):
    paciente = db.get_paciente(id)

    if paciente:
        dados = paciente[0]
        return edit.paciente_html(dados)
    else:     
        return ""