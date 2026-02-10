# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    
    #Define las paginas en las que se cambiara durante el proceso
    PAGE_LOGIN = 0
    PAGE_MAIN = 1

    def __init__(self):
        super().__init__()

        #La clase no sabe de que manera sirven estas ventanas, solo las usa
        self.login_view = LoginView()
        self.main_view = MainView()


        #Es el servicio que permite autenticar a los usuarioa
        self.auth_service = AuthService()
        
        #Aqui se presenta parte de la estructura del login, es el presentador de esta
    
        self.login_presenter = LoginPresenter(
            view=self.login_view,       #El presenter escucha lo que sucede en el login
            auth=self.auth_service,     #El presenter llama a los servicios de autenticacion
            on_success=self._go_main    #Si la autenticacion es valida llama a esa funcionn
        )
        
        self.addWidget(self.login_view)
        self.addWidget(self.main_view)
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(700, 700)
        
    def _go_main(self, username: str):
        self.main_view.set_welcome(username)
        self.setCurrentIndex(self.PAGE_MAIN)
