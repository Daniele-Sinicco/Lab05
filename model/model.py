from database.corso_DAO import get_corsi_dao
from database.studente_DAO import get_studenti_dao
from database.studente_DAO import get_iscritti_dao
from database.studente_DAO import get_spec_stud_dao
from database.corso_DAO import get_corsi_stud_dao
from database.studente_DAO import get_iscritto_dao
class Model:
    def __init__(self):
        pass

    def get_lista_studenti(self):
        return get_studenti_dao()

    def get_lista_corsi(self):
        return get_corsi_dao()

    def get_lista_iscritti(self, cod_corso):
        return get_iscritti_dao(cod_corso)

    def get_spec_stud(self, matr):
        return get_spec_stud_dao(matr)

    def get_corsi_stud(self, matr):
        return get_corsi_stud_dao(matr)

    def iscrizione(self, matr, cod_corso):
        get_iscritto_dao(matr, cod_corso)
