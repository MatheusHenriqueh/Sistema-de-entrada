#Sistema de entrada
#Autor: Matheus Ruivo
#Data: 15/10/25
#Treinando and
print("Carregando..")
nome = input("Qual é seu nome?")
cracha = input("Qual o número do seu cracha?")
hora = input("Qual a hora de sua entrada?")

numero = '123' 
tempo = '7:30'

if cracha == numero and hora == tempo:# cracha é igual a número (sim), hora é igual a tempo (sim).
    print(f"Bem-vindo {nome}, acesso liberado!")#Então, o if vai ser executado, se alguma parte do if for false, não vai ser nada executado.
else:
    print(f"Acesso negado, revise {nome}!")