# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from database.DB_connect import get_connection

def get_corsi_dao():
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    result = []
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""SELECT * FROM corso""")
    for row in cursor:
        result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
    cursor.close()
    cnx.close()
    return result

def get_corsi_stud_dao(matr):
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    result = []
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""SELECT * FROM corso WHERE codins IN (SELECT codins FROM iscrizione WHERE matricola = %s)""", (matr,))
    for row in cursor:
        result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
    cursor.close()
    cnx.close()
    return result