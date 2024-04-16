import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        #self.txt_name = None
        self.dd_corsi = None
        self.btn_iscritti = None
        self.txf_matricola = None
        self.txf_nome = None
        self.txf_cognome = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        """self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )"""
        #row1
        self.dd_corsi = ft.Dropdown(label="corso", width=700, options=[])
        self._controller.load_dd()
        # button for the "hello" reply
        self.btn_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_stud_list)
        row1 = ft.Row([self.dd_corsi, self.btn_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #row2
        self.txf_matricola = ft.TextField(label="matricola", on_submit=self.clean_stud)
        self.txf_nome = ft.TextField(label="nome", read_only=True)
        self.txf_cognome = ft.TextField(label="cognome", read_only=True)
        row2 = ft.Row([self.txf_matricola, self.txf_nome, self.txf_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #row3
        self.btn_cerca_stud = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_stud_search)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_course_search)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        row3 = ft.Row([self.btn_cerca_stud, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def clean_stud(self, e):
        self.txf_nome.value = ""
        self.txf_cognome.value = ""
        self.update_page()
