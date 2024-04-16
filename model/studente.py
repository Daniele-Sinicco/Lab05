class Studente:
    def __init__(self, matricola, cognome, nome, CDS):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.CDS = CDS

    def __str__(self):
        return f'{self.matricola} {self.cognome} {self.nome} {self.CDS}'