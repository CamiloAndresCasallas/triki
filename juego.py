from jugador import Jugador
from tablero import Tablero
class Juego:
    def _init_(self):

         self.miJugador= Jugador("humano")

         self.Computador=Jugador("cpu")
         self.miTablero= Tablero()
    
    def jugarTriqui(self):
       
        self.miJugador.seleccionar_simbolo()

        if self.miJugador.miFicha.simbolo=='X':
            self.Computador.miFicha.simbolo='O'
        else:
            self.Computador.miFicha.simbolo='X'  

        jugadas=0
        
        while jugadas<9:
            self.miJugador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_triqui():
               self.miTablero.mostrar_tablero()
               print("Ganador")
               return True
            self.Computador.realizar_jugada(self.miTablero)
            if self.miTablero.verificar_triqui():
                self.miTablero.mostrar_tablero()
                print("Perdedor")
                return True
            jugadas=jugadas+1
            self.miTablero.mostrar_tablero()
           
miJuego=Juego()
miJuego.jugarTriqui()