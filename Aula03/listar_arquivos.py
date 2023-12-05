import os 

os.system("cls")

lst = (os.listdir("c:/"))

ps = 1

for i in lst:
    print(str(ps)+"º - "+i)
    ps+=1

esc = input("Digite o número correspondente a pasta que deseja ver: ")

match esc: 
    case "1":
        print(os.listdir("c:/$Recycle.Bin"))

    case "2":
        print(os.listdir("c:/$WinREAgent"))

    case "3":
        print(os.listdir("c:/6D1651A4F4A4"))

    case "4":
        print(os.listdir("c:/Arquivos de Programas") )

    case "5":
        print(os.listdir("c:/Documents and Settings"))

    case "6":
        print(os.listdir("c:/DumpStack.log.tmp"))

    case "7":
        print(os.listdir("c:/HashiCorp"))

    case "8":
        print(os.listdir("c:/hiberfil.sys"))

    case "9":
        print(os.listdir("c:/Intel"))

    case "10":
        print(os.listdir("c:/jee-2022-12"))

    case "11":
        print(os.listdir("c:/npm"))

    case "12":
        print(os.listdir("c:/NVIDIA")  )

    case _:
        print("Diretório não localizado")         
