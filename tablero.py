class Tablero:

    
    def __init__(self):
        self.matriz=[["","",""],["","",""],["","",""]]
        
        
    def verificar_jugada(self,x,y):
        if x== -1:
            return False
        if self.matriz[x][y]=="":
            return True
        else:
            return False
            
            
    
    def verificar_triki(self):
        
        self.verificar_filas()
        self.verificar_columnas()
        
        
    def verificar_columnas(self):
        i=0
        while i<3:
            if self.matriz[0][i]==self.matriz[1][i]==self.matriz[2][i]:
                triqui=True
            i=i+1
            return triqui
    def verificar_filas(self):
        i=0
        while i<3:
            if self.matriz[i][0]==self.matriz[i][1]==self.matriz[i][2]:
                triqui=True
            i=i+1
            return triqui
    
    def verificar_diagonales(self):
        if self.matriz[0][0]==self.matriz[1][1]==self.matriz[2][2] or self.matriz[0][2]==self.matriz[1][1]==self.matriz[2][0]:
            triqui=True   
            return triqui

    def mostrar_tablero(self):
        print(self.matriz)
        
mitablero=Tablero()
mitablero.mostrar_tablero()