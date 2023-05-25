#==========IMPORTAÇÃO============
import random
#==========VARIÁVEIS============
vitoria = '\033[1;;42m'
empate = '\033[1;;43m'
fecha = '\033[m'
t = '\033[7;34m'
pjoga = '\033[1;34m'
mjoga = '\033[1;31m'
m = '\033[;31m'
n = (random.randint(1,3))
a1 = '🗻'
a2 = '🧻'
a3 = '🪒'
#======================ENTRADA================================
print('='*10,f'{t}JOGO:PEDRA PAPEL E TESOURA{fecha}','='*10)
print("""[1] PEDRA
[2] PAPEL
[3] TESOURA""")
np = str(input('Qual você quer jogar? '))
#=====================PLAYER JOGA==============================
if np == '1':
    print(f'{pjoga}O PLAYER JOGA:{fecha} {pjoga}{a1}{fecha}!')
elif np == '2':
    print(f'{pjoga}O PLAYER JOGA:{fecha} {pjoga}{a2}{fecha}!')
elif np == '3':
    print(f'{pjoga}O PLAYER JOGA:{fecha} {pjoga}{a3}{fecha}!')
#=====================MÁQUINA JOGA==============================
if n == 1:
    print(f'{mjoga}A MÁQUINA JOGA:{fecha} {mjoga}{a1}{fecha}!')
elif n == 2:
    print(f'{mjoga}A MÁQUINA JOGA:{fecha} {mjoga}{a2}{fecha}!')
elif n == 3:
    print(f'{mjoga}A MÁQUINA JOGA:{fecha} {mjoga}{a3}{fecha}!')
#================RESULTADO MÁQUINA VENCEUU===============
if n == 2 and np == '1':
    print(f'{vitoria}Á MÁQUINA VENCEU O PLAYER!{fecha}')
elif n == 3 and np == '2':
    print(f'{vitoria}Á MÁQUINA VENCEU O PLAYER!{fecha}')
elif n == 1 and np == '3':
    print(f'{vitoria}Á MÁQUINA VENCEU O PLAYER!{fecha}')
#================RESULTADO PLAYER PLAYER=================
if np == '2' and n == 1:
    print(f'{vitoria}O PLAYER VENCEU À MÁQUINA!{fecha}')
elif np == '3' and n == 2:
    print(f'{vitoria}O PLAYER VENCEU À MÁQUINA!{fecha}')
elif np == '1' and n == 3:
    print(f'{vitoria}O PLAYER VENCEU À MÁQUINA!{fecha}')
#===========EMPATE===================
if n == 1 and np == '1':
    print(f'{empate}EMPATE!{fecha}')
if n == 2 and np == '2':
    print(f'{empate}EMPATE!{fecha}')
if n == 3 and np == '3':
    print(f'{empate}EMPATE!{fecha}')