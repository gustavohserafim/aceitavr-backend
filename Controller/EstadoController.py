from Model.Estado import Estado
from fastapi.encoders import jsonable_encoder


class EstadoController:

    def __init__(self, id):
        self.id = id

    @staticmethod
    def get_all():
        return jsonable_encoder(Estado.all())

    def get(self):
        return jsonable_encoder(Estado(self.id).get_by_id())