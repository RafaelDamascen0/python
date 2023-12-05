from classe_dog import dog

# para criar o objeto, utilizamos a variavel 
# pincher e realizamos o processo de 
# intanciação de classe dog.
# foi passado o nome e a idade

pincher = dog("negodoce",5)
# acessamos o método data_dog que mostra 
# os dados do cachorro
pincher.data_dog()
pincher.sit()
pincher.roll_over()
print(pincher.__class__)
print(pincher.__dict__)