import os 

os.system("cls")
print("Temos dois arquivos: bloco_texto.text e dados.txt")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto\n - 2 para olaa\n: ")

p = input("Você realmente deseja apagar o arquivo?[s,n] ")
if p == "s":
    if es == "1":
        os.remove("bloco_texto.txt")
    else:
        os.remove("ola.txt")
    print("O arquivo foi apagado com sucesso!")
else:
    print("Operação cancelada")
