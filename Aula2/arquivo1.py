# Importar a biblioteca os(sistema operacional)
import os

#limpar a tela 
os.system("clear")

arq = open("./texto.txt","w")
arq.write("Hoje é quarta-feira\nultima semana de novembro")
arq.close()