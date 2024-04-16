import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def load_dd(self):
        corsi = self._model.get_lista_corsi()
        for c in corsi:
            self._view.dd_corsi.options.append(ft.dropdown.Option(key=c.codins, text=c.__str__()))
        self._view.update_page()

    def handle_stud_list(self, e):
        if self._view.dd_corsi.value == None:
            self._view.create_alert("Inserire il corso!")
            return
        studenti = self._model.get_lista_iscritti(self._view.dd_corsi.value)
        self._view.txt_result.clean()
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s.__str__()))
        self._view.update_page()

    def handle_stud_search(self, e):
        if self._view.txf_matricola.value == "":
            self._view.create_alert("Inserire la matricola!")
            return
        studente = self._model.get_spec_stud(int(self._view.txf_matricola.value))
        if studente == None:
            self._view.create_alert("Studente non trovato :(")
        else:
            self._view.txf_nome.value = studente.nome
            self._view.txf_cognome.value = studente.cognome
            self._view.update_page()

    def handle_course_search(self, e):
        self.handle_stud_search(e)
        self._view.txt_result.clean()
        corsi = self._model.get_corsi_stud(int(self._view.txf_matricola.value))
        for c in corsi:
            self._view.txt_result.controls.append(ft.Text(c.__str__()))
        self._view.update_page()

    def handle_iscrivi(self, e):
        if self._view.dd_corsi.value == None or self._view.txf_matricola.value == "":
            self._view.create_alert("Selezionare corso e inserire matricola!")
            return
        self.handle_stud_search(e)
        self._view.txt_result.clean()
        lista_iscritti = self._model.get_lista_iscritti(self._view.dd_corsi.value)
        for s in lista_iscritti:
            if s.matricola == int(self._view.txf_matricola.value):
                self._view.create_alert("Studente già iscritto!")
                return
        self._model.iscrizione(int(self._view.txf_matricola.value), self._view.dd_corsi.value)
        self._view.txt_result.controls.append(ft.Text(f'Lo studente {self._view.txf_cognome.value} {self._view.txf_nome.value} {self._view.txf_matricola.value} è stato iscritto al corso {self._view.dd_corsi.value}.'))
        self._view.update_page()
