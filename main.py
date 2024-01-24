from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/app", StaticFiles(directory="static", html="true"), name="static")

@app.get("/", response_class=RedirectResponse)
async def root():
    return "/app/login.html"

@app.get("/api")
async def api():
    return {"dados": "Lista de medicos"}