""" 
Assim como em outros estruturas em Python, os dicionários
possuem métodos que agilizam e facilitam a manipulação dele
dentro do Python.

"""

alunos = {
    "aluno1": {"nome": "João", "idade": 20, "curso": "Engenharia"},
    "aluno2": {"nome": "Maria", "idade": 22, "curso": "Medicina"},
    "aluno3": {"nome": "Pedro", "idade": 19, "curso": "Direito"}
} 

# Método clear(): Limpa todo o dicionário

alunos.clear() # alunos = {} 


# Método copy(): Copia todo o dicionário para dentro de outra variável que está em outro espaço da memória

alunos_copia = alunos.copy()


# Método get(): Serve para acessar um valor dentro do dicionário, mas ele retorna esse valor 

alunos.get('aluno1') # {"nome": "João", "idade": 20, "curso": "Engenharia"}

alunos.get('alunos4') # None - Se for uma chave que não existe ele retorna None

alunos.get('alunos4', 'NÃO TEM') # NÃO TEM - podemos personalizar o valor de retorno quando é None


# Método keys(): Retorna uma tupla de lista com todas as chaves contidas no dicionário

alunos.keys() # dict_keys(['aluno1', 'aluno2', 'aluno3'])


# Método setdefault(): Adiciona um valor no dicionário caso esse valor não exista, se existir não faz nada

alunos.setdefault("alunos 4", {'nome':"Pedro", 'idade':19, 'curso':"Direito"})


# Método update(): Atualiza ou adiciona ao seu dicionário outro dicionário 

alunos.update({"alunos 4":{'nome':"kauã", "idade":20, 'curso':'Engenharia'}}) #atualizei o dicionário aluno4

alunos.update({'aluno 5':{'nome':'Amanda', 'idade':20, 'curso':'Programação'}}) # adicionei mais uma chave ao dicionário


# Método in(): Verifica se uma chave é pertencente a um dicionário, retornando True ou False

'aluno 1' in alunos # True
'aluno 5' in alunos # False
"nome" in alunos["aluno1"] # True - Faz a verificação no dicionário interno



