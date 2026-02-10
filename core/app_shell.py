# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.professor_view import ProfessorView
from ui.student_view import StudentView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter
from ui.admin_view import AdminView

class AppShell(QStackedWidget):
    
    #Define las paginas en las que se cambiara durante el proceso
    PAGE_LOGIN = 0
    PAGE_STUDENT = 1
    PAGE_PROFESSOR = 2
    PAGE_ADMIN = 3

    def __init__(self):
        super().__init__()

        #La clase no sabe de que manera sirven estas ventanas, solo las usa
        self.login_view = LoginView()
        self.student_view = StudentView()
        self.professor_view = ProfessorView()
        self.admin_view = AdminView()


        #Es el servicio que permite autenticar a los usuarioa
        self.auth_service = AuthService()
        
        #Aqui se presenta parte de la estructura del login, es el presentador de esta
    
        self.login_presenter = LoginPresenter(
            view=self.login_view,       #El presenter escucha lo que sucede en el login
            auth=self.auth_service,     #El presenter llama a los servicios de autenticacion
            on_success=self._go_main    #Si la autenticacion es valida llama a esa funcionn
        )
        
        
    #Aqui se indican las vistas
        self.addWidget(self.login_view)         
        self.addWidget(self.student_view)#Estas dos lineas anteriores registran las dos ventanas
        self.addWidget(self.professor_view)
        self.addWidget(self.admin_view)
        
        self.setCurrentIndex(self.PAGE_LOGIN)   #Pero se inicia siempre la pagina del login
        self.setWindowTitle("PyQt5 - MVP")      #Texto superior de la ventana
        self.resize(700, 700)                   #Dimensiones de la pantalla
        
    #La funcion que se invoca cuando el registro es correcto       
    def _go_main(self, username: str, role: str):
        if role == "student":
            self.student_view.set_user(username)
            self.setCurrentIndex(self.PAGE_STUDENT)
        elif role == "professor":
            self.professor_view.set_user(username)
            self.setCurrentIndex(self.PAGE_PROFESSOR)
        elif role == "administrator":
            self.admin_view.set_user(username)
            self.setCurrentIndex(self.PAGE_ADMIN)
