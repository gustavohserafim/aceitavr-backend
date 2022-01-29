from App.DB import DB


class Categoria:

    def __init__(self, id):
        self.id = id

    def get_by_id(self):
        return DB().run_fr("SELECT nome FROM categoria WHERE removed = 0 AND id = {};".format(self.id))

    @staticmethod
    def all():
        return DB().run_fa("SELECT nome FROM categoria WHERE removed = 0;")
