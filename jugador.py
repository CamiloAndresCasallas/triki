from ficha import Ficha
import random

class Jugador:
    def __init__(self):
        self.mificha=Ficha()
        
    def seleccionar_simbolo(self):
        x=random.randint(0,1)
        if x==0:
            self.mificha.simbolo="O"
            
        else:
            self.mificha.simbolo="X"
        
    def realizar_jugada(self,mitablero):
        x=int(input("Seleccione una fila: "))
        y=int(input("Seleccione una columna: "))
        
        mitablero.matriz[x][y]=self.mificha.simbolo
                
        
        