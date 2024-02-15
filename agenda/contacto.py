
class Contacto:
    
    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"