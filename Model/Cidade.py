from App.DB import DB


class Cidade:

    def __init__(self, id):
        self.id = id

    @staticmethod
    def all():
        return DB().run_fa("SELECT nome FROM cidade WHERE active = 1;")

    def get_by_id(self):
        return DB().run_fr("SELECT nome, active FROM cidade WHERE id = {};".format(self.id))
