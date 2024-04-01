from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

import json
import time
import urllib.parse as html

import db
import db_init

# import static.fragments.html_add as add
# import static.fragments.html_edit as edit

ERR_MSG = "Todos os campos precisam ser preenchidos!!!"
LEN_PAGE = 5

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

    body.pop("page", None)
    return body


async def get_params(req: Request):
    payload = req.query_params

    try:
        params = dict(payload)
    except:
        params = None
    return params


@app.get("/", response_class=RedirectResponse)
async def root():
    return "/app/login.html"


@app.get("/api", response_class=RedirectResponse)
async def api():
    return "/app/login.html"


# PACIENTES-------------------------------------------------------
@app.get("/api/pacientes", response_class=JSONResponse)
async def pacientes():
    dados = db.get_pacientes()
    # time.sleep(1)
    return dados


@app.get("/api/pacientes/{id}", response_class=JSONResponse)
async def paciente(id: int):
    dados = db.get_paciente(id)
    return dados


@app.post("/api/pacientes", response_class=JSONResponse)
async def add_paciente(body=Depends(get_body)):
    if is_valid(body, 15):
        db.add_paciente(body)
        dados = db.get_pacientes()
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/pacientes/search", response_class=JSONResponse)
async def get_pacientes(body=Depends(get_body)):
    search = body["search"]
    dados = db.get_pacientes() if len(search) < 2 else db.search_pacientes(search)
    return dados


@app.put("/api/pacientes/{id}", response_class=JSONResponse)
async def update_paciente(id: int, body=Depends(get_body)):
    if is_valid(body, 15):
        db.update_paciente(id, body)
        dados = db.get_pacientes()
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.delete("/api/pacientes/{id}", response_class=HTMLResponse)
async def del_paciente(id: int):
    db.del_paciente(id)
    return


# MEDICOS-----------------------------------------------------------
@app.get("/api/medicos", response_class=JSONResponse)
async def medicos(params=Depends(get_params)):
    if params:
        key = "page"
        page = int(params[key] if key in params else 0)
        page = 0 if page < 0 else page
        dados = db.get_medicos_paged(LEN_PAGE, page)
        return dados
    else:
        return db.get_medicos()


@app.get("/api/medicos/{id}", response_class=JSONResponse)
async def medico(id: int):
    dados = db.get_medico(id)
    return dados


@app.post("/api/medicos", response_class=JSONResponse)
async def add_medico(body=Depends(get_body)):
    if is_valid(body, 15):
        nome = body["nome"]
        db.add_medico(body)
        dados = db.get_medicos_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/medicos/search", response_class=JSONResponse)
async def get_medicos(body=Depends(get_body)):
    busca = body["search"]
    dados = db.get_medicos() if len(busca) < 2 else db.search_medicos(busca)
    return dados


@app.put("/api/medicos/{id}", response_class=JSONResponse)
async def update_medico(id: int, body=Depends(get_body)):
    if is_valid(body, 15):
        db.update_medico(id, body)
        nome = body["nome"]
        dados = db.get_medicos_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.delete("/api/medicos/{id}", response_class=HTMLResponse)
async def del_medico(id: int):
    db.del_medico(id)
    return


# RETORNA FRAGMENTOS DE HTML


# RETORNAR TEMPLATE PARA INCLUIR PACIENTES--------------------------------------
@app.get("/html/pacientes/new/add", response_class=HTMLResponse)
async def add_paciente():
    return fragment("paciente_add")


# RETORNAR TEMPLATE PARA INCLUIR MEDICOS-----------------------------------------
@app.get("/html/medicos/new/add", response_class=HTMLResponse)
async def add_medico():
    return fragment("medico_add")


# RETORNAR TEMPLATE PARA EDITAR PACIENTES-----------------------------------------
@app.get("/html/pacientes/{id}/edit", response_class=HTMLResponse)
async def edit_paciente(id: int):
    dados = db.get_paciente(id)
    html = fragment_format(dados, "paciente_edit")
    return html


# RETORNAR TEMPLATE PARA EDITAR MEDICOS-------------------------------------------
@app.get("/html/medicos/{id}/edit", response_class=HTMLResponse)
async def edit_medico(id: int):
    dados = db.get_medico(id)
    html = fragment_format(dados, "medico_edit")
    return html


# RETORNA DETALHE---------------------------------------------------------
@app.get("/html/pacientes/{id}/detalhe", response_class=HTMLResponse)
async def detalhe_paciente(id):
    dados = db.get_paciente(id)
    return fragment_format(dados, "paciente_detalhe")


@app.get("/html/medicos/{id}/detalhe", response_class=HTMLResponse)
async def detalhe_medico(id):
    dados = db.get_medico(id)
    return fragment_format(dados, "medico_detalhe")


# FUNÇÕES AUXILIARES E ENDPOINTS DE TESTE


# RESETAR O BANDO DE DADOS---------------------------------------------------------
@app.get("/reset", response_class=RedirectResponse)
def db_reset():
    db_init.tables_init()
    return "/app/home.html"


# ----------------------------------------------------------------------------------
def is_valid(body: dict, qtd: int):
    fields = sum([1 if v else 0 for _, v in body.items()])
    return fields == qtd


def fragment(frag):
    html = open(f"./static/fragments/{frag}.html", "r", encoding="utf-8").readlines()
    return "".join(html)


def fragment_format(dados, frag):
    if dados:
        html = fragment(frag)
        html = html.format(**dados[0])
        return html
    else:
        raise HTTPException(status_code=404)
