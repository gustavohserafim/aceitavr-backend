from Model.Cidade import Cidade
from fastapi.encoders import jsonable_encoder


class CidadeController:

    def __init__(self, id):
        self.id = id

    @staticmethod
    def get_all():
        return jsonable_encoder(Cidade.all())

    def get(self):
        return jsonable_encoder(Cidade(self.id).get_by_id())
