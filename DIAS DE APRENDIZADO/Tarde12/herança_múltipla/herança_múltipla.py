""" 
A herança múltipla é uma extensão da herança simples,
onde é passado dois parâmetros na classe filho.

Diagrama:

                  ANIMAL
                    ↑
           —— —— —— —— —— —— —— ——
           |                     |
       MAMÍFERO                 AVE
           ↑                     |
   —— —— —— —— —— —— —— —— —— —— | 
   |       |     |               |
  Cão    Gato  Leão        Ornitorrinco

"""

class animal(): # classe pai
    def __init__(self, numero_patas):
        self.nro_patas = numero_patas
        
    def exibir_patas(self):
        print(f"O número de patas é: {self.nro_patas}")

class mamifero(animal): # classe filha da classe animal
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw) # Todo atributo que estiver na classe animal já será passada
        self.cor_pelo = cor_pelo
        
    def exiir_pelo(self):
        print(f"A cor do pelo é: {self.cor_pelo}")
        
    

class ave(animal): # classe filha da classe animal
    def __init__(self, eh_domestico, **kw):
        
        
        super().__init__(**kw) #Todo atributo que estiver na classe animal já será passada
        self.eh_domestico = eh_domestico
    
    def eh_domestico_(self):
        print(f"{"Animal doméstico" if self.eh_domestico else "Animal selvagem"}")

class cão(mamifero): # classe filha da classe mamnifero e neta da classe animal
    pass

class gato(mamifero): # classe filha da classe mamnifero e neta da classe animal
    pass

class leão(mamifero): #classe filha da classe mamnifero e neta da classe animal
    pass

class ornitorrinco(ave, mamifero): # #classe filha da classe mamnifero, e também da classe ave e neta da classe animal
    pass



gato = gato(cor_pelo='Amarelo', numero_patas=4)
gato.exibir_patas()
gato.exiir_pelo()


leao = leão(cor_pelo='Bege', numero_patas=4)
leao.exiir_pelo()

ornito = ornitorrinco(numero_patas=4, cor_pelo='Ciano', eh_domestico=False)
ornito.exibir_patas()
ornito.exiir_pelo()
ornito.eh_domestico_()



# OBS: Ao se usar os **kw é preciso passar os argumentos por chave=valor