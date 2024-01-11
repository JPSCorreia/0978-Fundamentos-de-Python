
# if, else if e else
numero = 10
if numero % 2 == 0:
  print('par')
elif numero % 5 == 0:
  print('nao é par mas é divisivel por 5')
else:
  print('nao é par')

if numero % 2 == 0 and numero % 5 == 0:
  print('é par e divisivel por 5')

# case
nota = 42
match nota:
  case 10:
    print('nota de 10')
  case 15:
    print('nota de 15')
  case _:
    print('outra nota qualquer')

# funções
def ola_mundo():
  print('Olá mundo!')
ola_mundo()

def ola_mundo2(nome: str):
  print(f'Olá mundo!, sou eu o {nome}!')
ola_mundo2('João')
ola_mundo2(23)

def ola_mundo3(nome: str):
  return f'Olá mundo!, sou eu o {nome}!'
print(ola_mundo3('Maria'))

