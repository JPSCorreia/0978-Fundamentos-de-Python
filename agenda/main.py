from agenda import Agenda
from contacto import Contacto
import csv

# File path
file_path = './agenda/agenda.csv'

agenda = Agenda()

# Reading from the CSV file
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Iterate through rows
    for row in reader:
        # Each 'row' is a list representing a line in the CSV
        agenda.adicionarContacto(Contacto(row[0], row[1], row[2]))



# agenda.mostrarContactos()
agenda.adicionarContacto(Contacto("Armando", email="teste@teste.com", telefone="555-123-4567"))
agenda.apagarContacto("John Doe")
agenda.mostrarContactos()

while True:
    
    acao = "Diz a aão que desejas fazer\n1 - Mostrar contactos\n2 - Adicionar contacto\n3 - Apagar contacto\n4 - Editar Contacto\n* - Sair"
    
    match acao:
        case '1':
            agenda.mostrarContactos()
        case '2':
            agenda.adicionarContacto(Contacto(nome = input("Nome: "), email = input("Email: "), telefone = input("Telefone: ")))
        case '3':
            agenda.apagarContacto(nome = input("Nome: "))
        case '4':
            agenda.editarContacto()
        case '*':
            break

# Agenda deve:
#    - Adicionar um contacto - FEITO
#    - Procurar um contacto - FEITO
#    - Editar um contacto - FEITO
#    - Apagar um contacto - FEITO
#    - Mostrar todos os contactos - FEITO
#    - Mostrar um contacto - Feito
#    - Criar um menu de navegação
#    - Opção gravar - Escrever dados no array para um ficheiro csv
#    - 
#    - 
#    - 
#    - 
#    - 
#    - 
#    - 
#    - 
#    - 