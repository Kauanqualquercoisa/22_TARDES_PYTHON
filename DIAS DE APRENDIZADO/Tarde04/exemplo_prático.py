""" 
Exercício bastante ilustrativo para verificar essa 
importância da identação em Python e como usar isso
ao seu favor para construir programas complexos
com mais eficiência utlizando estruturas de condição 
com if's aninhados.

"""
# PEDRA, PAPEL OU TESOURA:  O programa deve ler a escolha do jogador.
# A e a escolha do jogador B. Por fim, o programa deve indicar quem foi o vencedor.


jogador_a = input('\nDigita sua jogada (Pedra, Papel ou Tesoura): ') # leitura de dados

jogador_b = input('\nDigita sua jogada (Pedra, Papel ou Tesoura): ') # leitura de dados

if jogador_a == 'Pedra': #jogador a escolhe Pedra e o b as outras possibilidades
    if jogador_b == 'Papel':
        print('\nJogador B é o vencedor!')
    elif jogador_b == 'Tesoura':
        print('\nJogador A é o vencedor!')
    else:
        print('\nEmpate!')
elif jogador_a == 'Papel': #jogador a escolhe Papel e o b as outras possibilidades
    if jogador_b == 'Pedra':
        print('\nJogador A é o vencedor!')
    elif jogador_b == 'Tesoura':
        print('\nJogador B é o vencedor!')
    else:
        print('\nEmpate!')
elif jogador_a == 'Tesoura': #jogador a escolhe Tesoura e o b as outras possibilidades
    if jogador_b == 'Pedra':
        print('\nJogador B é o vencedor!')
    elif jogador_b == 'Papel':
        print('\nJogador A é o vencedor!')
    else:
        print('\nEmpate!')