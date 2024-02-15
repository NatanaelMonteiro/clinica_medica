from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

import db
import db_init

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
    dados = db.get_pacientes()
    return JSONResponse(dados)


@app.get("/api/medicos", response_class=JSONResponse)
async def medicos(request: Request):
    return db.get_medicos()

@app.delete("/api/medicos/{id}", response_class=HTMLResponse)
async def del_medico(id: str):
    db.del_medico(id)
    return ""

@app.delete("/api/pacientes/{id}", response_class=HTMLResponse)
async def del_paciente(id: str):
    db.del_paciente(id)
    return ""

@app.get("/reset", response_class=RedirectResponse)
def db_reset():
    db_init.tables_init()
    return "/app/home.html"