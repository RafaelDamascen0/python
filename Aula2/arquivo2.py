import os
os.system("clear")

arq = open("./arquivos/dados.csv","a")
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
arq.write(nome+";"+email+"\n")
arq.close()