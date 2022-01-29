from fastapi import FastAPI

# Controllers
from Controller.EstadoController import EstadoController
from Controller.CidadeController import CidadeController
from Controller.CategoriaController import CategoriaController

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/estado")
async def estados():
    return EstadoController.get_all()


@app.get("/estado/{estado_id}")
async def estado(estado_id: int):
    return EstadoController(estado_id).get()


@app.get("/cidade")
async def cidades():
    return CidadeController.get_all()


@app.get("/cidade/{cidade_id}")
async def cidade(cidade_id: int):
    return CidadeController(cidade_id).get()


@app.get("/categoria")
async def categorias():
    return CategoriaController.all()


@app.get("/categoria/{categoria_id}")
async def categoria(categoria_id: int):
    return CategoriaController(categoria_id).get()
