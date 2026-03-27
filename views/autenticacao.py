from pydantic import BaseModel

class UsuarioOut(BaseModel):
    id: int
    login: str
    
class TokenOut(BaseModel):
    access_token: str
    token_type: str