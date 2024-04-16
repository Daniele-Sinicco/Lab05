# Add whatever it is needed to interface with the DB Table studente
from model.studente import Studente
from database.DB_connect import get_connection

def get_studenti_dao():
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    result = []
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""SELECT * FROM corso""")
    for row in cursor:
        result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
    cursor.close()
    cnx.close()
    return result

def get_iscritti_dao(cod_corso):
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    result = []
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""SELECT * FROM studente WHERE matricola IN (
                        SELECT matricola FROM iscrizione WHERE codins = %s)""", (cod_corso,))
    for row in cursor:
        result.append(Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"]))
    cursor.close()
    cnx.close()
    return result

def get_spec_stud_dao(matr):
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""SELECT * FROM studente WHERE matricola = %s""", (matr,))
    row = cursor.fetchone()
    cursor.close()
    cnx.close()
    if row:
        return Studente(row["matricola"], row["nome"], row["cognome"], row["CDS"])
    else:
        return None

def get_iscritto_dao(matr, cod_corso):
    cnx = get_connection()
    if cnx is None:
        print("Connection error")
        return
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("""INSERT INTO iscrizione(matricola, codins) VALUES (%s, %s)""", (matr, cod_corso))
    cnx.commit()
    cursor.close()
    cnx.close()
