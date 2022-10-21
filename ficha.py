class Ficha:
    
    def __init__(self):
        self.simbolo=""
        
        
    def set_simbolo(self,valor):
        self.simbolo=valor
        
mificha=Ficha()
mificha.set_simbolo("")
print(mificha.simbolo)