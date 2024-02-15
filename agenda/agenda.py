from contacto import Contacto

class Agenda:
    
    def __init__(self):
        self.listaDeContactos = []

    def adicionarContacto(self, contacto: Contacto):
        self.listaDeContactos.append(contacto)

    def mostrarContactos(self):
        for contacto in self.listaDeContactos:
            print(contacto)
    
    def apagarContacto(self, email):
        for contacto in self.listaDeContactos:
            if contacto.email == email:
                print(f'{contacto.nome} foi apagado')
                self.listaDeContactos.remove(contacto)
    
    def procurarContacto(self, nome):
        for contacto in self.listaDeContactos:
            if contacto.nome == nome:
                return contacto
        return print(f"Não existe o nome {contacto.nome} na sua agenda")
    
    def editarContacto(self, novo_nome, novo_email, novo_telefone):
        for contacto in self.listaDeContactos:
                contacto.nome = novo_nome
                contacto.email = novo_email
                contacto.telefone = novo_telefone
        return f"O contacto {contacto.nome} foi editado"

        #Adicionar na Edição do Contacto os parametros qeu o utilizador nao quer Editar!
                                    