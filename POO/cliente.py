# Declaração da classe Cliente. Esta classe permite
# Que sejam criados novos objeto do tipo cliente 
# A implementação do método __init__ representa a construção 
# do método construtor da classe, responsável or inicializar
# self que faz referência a própria classe. quando for
# criar um método de classe deve-se utilizar o comando 
# self para referenciaar a propria estrutura de classe a qual 
# ele pertence.
# Note que no método __init__(construtor) foram iniciados os 
# astributos da classe, representando as caracteristicas do cliente
# todos eles foram criados usando o comando self, que indica 
# que eles pertencem a classe Cliente. Os atributos foram 
# declarados como privados. Para isso utilizamos 2 undescores.

'''
 A classe Cliente gera novos Clientes e pede alguns 
 dados pessoais e é capaz de salvar o Cliente.
'''

class Cliente:

    


    def _init_(self):
     self.__nome = ""
     self.__idade = 0
     self.__genero = ""
     self.__email = ""

    # O método dados é utilizado para realizar a passagem dos dados 
    # do cliente para dentro da classe Cliente.
    def dados(self,nome="",idade=0,genero="",email=""):
        '''
        O metodo dados pede algumas informações do cliente para ele 
        seja salvo no sistema
        '''
        print()
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.email = email
    # O método gravar exibir uma mensagem com o do cliente
    # dizendo que foi salvo com sucesso 
    def gravar(self):
        '''
        O método gravar e exibe uma mensagem com o nome cliente e gravação 
        realizada com sucesso.
        '''
        print("O cliente "+self.nome+" foi gravado com sucesso")
        