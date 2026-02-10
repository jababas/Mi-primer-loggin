# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str | None = None

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        self._users = {
            
            "admin":    {"password": "1234", "role": "administrator"},
            "alumno":   {"password": "1234", "role": "student"},
            "profesor": {"password": "1234", "role": "professor"},
        }
        

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        
        if username not in self._users:
            return AuthResult(False, "Usuario no existe.")

        user = self._users[username]

        if password != user["password"]:
            return AuthResult(False, "Contraseña incorrecta.")

        return AuthResult(
            ok=True,
            message="Autenticación exitosa.",
            role=user["role"]
        )
