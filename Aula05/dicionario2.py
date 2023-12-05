capitais = {
    "Acre":"Rio branco",
    "Alagoas":"Maceio",
    "Amazonas":"Manaus",
    "Bahia":"Salvador",
    "Ceará":"Fortaleza",
    "Espírito Santo":"Vitoria",
    "Goiás":"Goiânia",
    "Maranhão":"São Luis",
    "Mato Grosso":"Cuiabá",
    "Mato Grosso do Sul":"Campo Grande",
    "Minas Gerais":"Belo Horizonte",
    "Pará":"Belém",
    "Paraibá":"João Pessoa",
    "Paraná":"Curitiba",
    "Pernambuco":"Recife",
    "Piauí":"Teresina",
    "Rio de Janeiro":"Rio de Janeiro",
    "Rio Grande do Norte":"Natal",
    "Rio Grande do Sul":"Porto Alegre",
    "Rondônia":"Porto Velho",
    "Roraima":"Boa vista",
    "Santa Catarina":"Florianópolis",
    "São Paulo":"São Paulo",
    "Sergipe":"Aracaju",
    "Tocantins":"Palmas",
    "Destrito Federal":"Brasilia",
}

# for i in capitais:
# print(i)

# print(capitais[0:6])
print(capitais["Acre"])
#pegar os 6 primeiros itens
ps = 1 
for i in capitais:
    if ps < 6:
        print(i+" A capital é "+capitais[i])
    else:
        break
    ps+=1
