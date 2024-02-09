from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse

import db

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
async def medicos(id: str):
    return ""

@app.delete("/api/pacientes/{id}", response_class=HTMLResponse)
async def pacientes(id: str):
    return ""