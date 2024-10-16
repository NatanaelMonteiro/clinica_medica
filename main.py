from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import (
    JSONResponse,
    RedirectResponse,
    HTMLResponse,
    PlainTextResponse,
)

import json

# import time
import urllib.parse as html

import db


LOGIN_ERR_MSG = "Usuário ou senha inválidos!"
ERR_MSG = "Todos os campos precisam ser preenchidos!"
LEN_PAGE = 5

app = FastAPI(
    title="Clínica Mentalis",
    version="0.5.1",
    summary="Protótipo de uma API para gestão de uma clínica médica. ",
)

app.mount("/app", StaticFiles(directory="static", html="True"), name="static")


async def get_body(req: Request):
    payload = await req.body()
    payload = payload.decode("utf8")
    payload = html.unquote(payload)

    try:
        if payload:
            body = json.loads(payload)
        else:
            body = {}

    except Exception as e:
        print(e)
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


@app.get("/info/title", response_class=PlainTextResponse)
def get_info():
    return app.title


@app.get("/api", response_class=RedirectResponse)
async def api_root():
    return "/app/login.html"


# @app.get("/api/capitulo", response_class=JSONResponse)
# async def capitulo():
#     return {"capitulo": sort_chapter()}


# @app.get("/api/usuarios", response_class=RedirectResponse)
# async def get_usuarios():
#     dados = db.get_usuarios()
#     return dados


@app.post("/api/usuarios")
async def usuario(body=Depends(get_body)):
    dados = body and db.is_usuario(body)
    if dados:
        return "<script>location.href='home.html'</script>"
    else:
        raise HTTPException(status_code=403, detail=LOGIN_ERR_MSG)


@app.get("/api/pacientes", response_class=JSONResponse)
async def pacientes(params=Depends(get_params)):
    page = 0

    if params:
        key = "page"
        page = int(params[key]) if key in params else 0
        page = 0 if page < 0 else page

    dados = db.get_pacientes_paged(LEN_PAGE, page)
    return dados


@app.get("/api/pacientes/{id}", response_class=JSONResponse)
async def paciente(id: int):
    dados = db.get_paciente(id)
    return dados


@app.put("/api/pacientes/{id}", response_class=JSONResponse)
async def update_paciente(id: int, body=Depends(get_body)):
    if is_valid(body, 15):
        nome = body["nome"]
        db.update_paciente(id, body)
        dados = db.get_paciente_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/pacientes", response_class=JSONResponse)
async def add_paciente(body=Depends(get_body)):
    if is_valid(body, 15):
        nome = body["nome"]
        db.add_paciente(body)
        dados = db.get_paciente_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/pacientes/search", response_class=JSONResponse)
async def search_pacientes(body=Depends(get_body)):
    key = "search"
    search = body[key] if key in body else ""

    if not search:
        dados = db.get_pacientes_paged(LEN_PAGE)

    elif len(search) > 1:
        dados = db.search_pacientes(search)

    else:
        # dados = db.get_pacientes_paged(LEN_PAGE)
        raise HTTPException(status_code=204)

    return dados


@app.delete("/api/pacientes/{id}", response_class=HTMLResponse)
async def del_paciente(id: int):
    db.del_paciente(id)
    return ""


@app.get("/api/medicos", response_class=JSONResponse)
async def medicos(params=Depends(get_params)):
    page = 0

    if params:
        key = "page"
        page = int(params[key]) if key in params else 0
        page = 0 if page < 0 else page

    dados = db.get_medicos_paged(LEN_PAGE, page)
    return dados


@app.get("/api/medicos/{id}", response_class=JSONResponse)
async def medico(id: int):
    return db.get_medico(id)


@app.put("/api/medicos/{id}", response_class=JSONResponse)
async def update_medico(id: int, body=Depends(get_body)):
    if is_valid(body, 15):
        nome = body["nome"]
        db.update_medico(id, body)
        dados = db.get_medico_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/medicos", response_class=JSONResponse)
async def add_medico(body=Depends(get_body)):
    if is_valid(body, 15):
        nome = body["nome"]
        db.add_medico(body)
        dados = db.get_medico_position(nome, LEN_PAGE)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.post("/api/medicos/search", response_class=JSONResponse)
async def search_medicos(body=Depends(get_body)):
    key = "search"
    search = body[key] if key in body else ""

    if len(search) > 1:
        dados = db.search_medicos(search)
    else:
        dados = db.get_medicos_paged(LEN_PAGE)

    return dados


@app.delete("/api/medicos/{id}")
async def del_medico(id: int):
    db.del_medico(id)
    return HTMLResponse(status_code=200)


@app.get("/api/consultas", response_class=JSONResponse)
async def get_consultas(param=Depends(get_params)):
    order = int(param["order"]) if param else 0
    dados = db.get_consultas(order)
    return dados


@app.get("/api/consultas/agendadas", response_class=JSONResponse)
async def get_consultas(param=Depends(get_params)):
    order = int(param["order"]) if param else 0
    dados = db.get_consultas(order, is_agendadas=True)
    return dados


@app.post("/api/consultas", response_class=JSONResponse)
async def add_consulta(body=Depends(get_body)):
    body.pop("search", None)

    if is_valid(body, 4) or is_valid(body, 5):
        body.update({"status": "agendada"})
        db.add_consulta(body)
        dados = db.get_consultas(tp_order=0, is_agendadas=True)
        return dados
    else:
        raise HTTPException(status_code=422, detail=ERR_MSG)


@app.patch("/api/consultas/{id}")
async def close_consulta(id: int):
    db.close_consulta(id)
    return HTMLResponse(status_code=200)


# @app.patch("/api/consultas/cancelar/{id}")
# async def del_consulta(id: int):
#     db.del_consulta(id)
#     return HTMLResponse(status_code=200)


@app.delete("/api/consultas/{id}")
async def del_consulta(id: int):
    db.del_consulta(id)
    return HTMLResponse(status_code=200)


# -------------------------------------- #
#       RETORNA FRAGMENTOS DE HTML       #
# -------------------------------------- #


# retornar template para incluir paciente
@app.get("/html/pacientes/new/add", response_class=HTMLResponse)
async def add_paciente():
    html = fragment("paciente_add")
    return "".join(html)


# retornar template para editar paciente
@app.get("/html/pacientes/{id}/edit", response_class=HTMLResponse)
async def edit_paciente(id: int):
    dados = db.get_paciente(id)
    return fragment_format("paciente_edit", dados)


# retornar template para exibir detalhes do paciente
@app.get("/html/pacientes/{id}/detalhe", response_class=HTMLResponse)
async def detalhe_paciente(id: int):
    dados = db.get_paciente(id)
    return fragment_format("paciente_detalhes", dados)


# retornar template para incluir medico
@app.get("/html/medicos/new/add", response_class=HTMLResponse)
async def add_medico():
    html = fragment("medico_add")
    return html


# retornar template para editar medico
@app.get("/html/medicos/{id}/edit", response_class=HTMLResponse)
async def edit_medico(id: int, params=Depends(get_params)):
    key = "page"
    page = params[key] if (params and key in params) else 0
    dados = db.get_medico(id)
    html = fragment_format("medico_edit", dados, page)
    return html


# retornar template para exibir detalhes do paciente
@app.get("/html/medicos/{id}/detalhe", response_class=HTMLResponse)
async def detalhe_medico(id: int):
    dados = db.get_medico(id)
    return fragment_format("medico_detalhes", dados)


# retornar template para incluir consulta
@app.get("/html/consulta/new/add", response_class=HTMLResponse)
async def add_consulta():
    html = fragment("consulta_add")
    return "".join(html)


# retorna um fragmento com o menu do sistema #
@app.get("/html/menu", response_class=HTMLResponse)
def get_menu():
    html = fragment("menu")
    return html


# --------------------------------------- #
# FUNÇÕES AUXILIARES E ENDPOINTS DE TESTE #
# --------------------------------------- #


# resetar o banco de dados
@app.get("/reset", response_class=RedirectResponse)
def db_reset():
    import db_init

    db_init.tables_init()
    return "/app/home.html"


def is_valid(body: dict, qtd: int):
    fields = sum([1 if v else 0 for _, v in body.items()])
    return fields == qtd


def fragment(frag):
    html = open(f"./static/fragments/{frag}.html", "r").readlines()
    return "".join(html)


def fragment_format(frag, dados, page=0):
    if dados:
        html = fragment(frag)
        return html.format(**dados[0])
    else:
        raise HTTPException(status_code=404)


def sort_chapter():
    import random as r

    chapter = [1, 2, 14, 15, 23, 24, 91, 100, 133, 150][r.randint(0, 9)]
    return chapter
