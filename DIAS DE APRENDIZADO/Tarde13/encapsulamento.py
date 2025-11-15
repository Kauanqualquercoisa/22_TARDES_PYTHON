""" 
O encapsulamento descreve a ideia de agrupar dados e os métodos que manipulam esses dados 
em uma unidade, impondo restrições ao acesso direto a variáveis e métodos, o que evita a 
modificação acidental de dados. 

Assim, para evitar alterações acidentais, a variável de um objeto só pode ser alterada 
pelo método desse objeto.

Em Python, o encapsulamento é implementado usando convenções de nomenclatura para indicar 
diferentes níveis de acesso:

(public) – acessível de qualquer lugar.

(protected) – indicado por um _underscore, sugere que o atributo/método não deve ser acessado 
diretamente fora da classe, mas ainda pode ser.
 
(private) – indicado por __dunder (double underscore), tornando mais difícil o acesso direto 
ao atributo.

"""

# exemplo de uso de encapsulamento

class banco():
    def __init__(self, saldo2, saldo1=0):
        self._saldo1 = saldo1 # _saldo indica que é um atributo protegido, não deve ser acesso diretamente
        
        self.__saldo2 = saldo2 # __saldo indica que é um atributo privado, não é possível acessá-lo
        
    def depositar(self, valor):
        
        """Método público para depositar dinheiro."""
        
        if valor > 0:
            self.__saldo2 += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        
        """Método público para sacar dinheiro, respeitando o saldo disponível."""
        
        if 0 < valor <= self.__saldo2:
            self.__saldo2 -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def verificar_saldo(self):
        
        """Método público para verificar saldo disponível."""
        
        return f"Saldo atual: R${self.__saldo2:.2f}"
        
        
conta = banco(50, 100)

print(conta._saldo1) # A saída será 100, porém não deveria ser acessada dessa forma    

#print(conta.__saldo2) # Erro: object has no attribute '__saldo2', pois é um atributo privado da classe

print(conta._banco__saldo2) # forma alternativa de forçar o acesso a um atributo privado

# forma correta de usar o código

conta.depositar(50) # deposita 50 reais, fazendo o saldo ser 100

conta.sacar(20) # saca 20 reais, fazendo o saldo ser 80


""" 
Para permitir o acesso aos atributos protegidos de uma maneira controlada, a prática mais comum 
é criar dois métodos, um para  retornar o valor e outro para alterar o valor. 
"""
print(conta.verificar_saldo())
