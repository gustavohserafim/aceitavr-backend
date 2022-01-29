from Model.Categoria import Categoria
from fastapi.encoders import jsonable_encoder


class CategoriaController:

    def __init__(self, id):
        self.id = id

    def get(self):
        return jsonable_encoder(Categoria(self.id).get_by_id())

    @staticmethod
    def all():
        return jsonable_encoder(Categoria.all())