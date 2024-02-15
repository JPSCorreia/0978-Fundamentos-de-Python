# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. 

class TV:

    def __init__(self, canal, volume):
        self.canal = max(0, min(canal, 50))
        self.volume = max(0, min(volume, 100))
        
    def mudarCanal(self, novoCanal):
        if (novoCanal >= 0 and novoCanal <= 50):
            self.canal = novoCanal
        else:
            print('erro, canal inválido.')

    def aumentarVolume(self, valor):
        self.volume = max(0, min(self.volume + valor, 100))

    def diminuirVolume(self, valor):
        self.volume = max(0, min(self.volume - valor, 100))

    def __str__(self):
        return f"Canal {self.canal}, volume {self.volume}."

# Testes
tv1= TV(1, 50)
tv1.aumentarVolume(10)
print(tv1)
tv1.aumentarVolume(90)
print(tv1)
tv1.diminuirVolume(80)
print(tv1)
tv1.diminuirVolume(50)
print(tv1)
tv1.mudarCanal(60)
print(tv1)
tv1.mudarCanal(30)
print(tv1)


