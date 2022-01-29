from App.DB import DB

class Estado:

    def __init__(self):
        pass

    @staticmethod
    def all():
        return DB().run_fa("SELECT nome, UF FROM estado;")

    def get_by_id(self):
        return DB().run_fr("SELECT nome, UF FROM estado WHERE id = {};".format(self.id))
