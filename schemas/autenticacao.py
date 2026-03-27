from pydantic import BaseModel

class UsuarioIn(BaseModel):
    login: str
    senha: str
    
