opcao = int(input('''
-------------------------------------------------
[1] Cadastrar
[2] Localizar
[3] Editar
[4] Deletar
------------------------------------------------
Digite uma das opções acima: ''')) # Para o usuário escolher uma das opções acima
  
def cadastrar(): # Função de cadastro
  
  if opcao == 1: # Caso se o usuário escolher a alternativa 1
    print('')
    nome = input('Digite o nome do produto: ')
    codigo = int(input('Digite o código do produto: '))
    preço = float(input('Digite o preço do produto: '))
    print('''\nNome:{}
Código:{}
Preço:R${}
          
Produto cadastrado com sucesso!\n'''.format(nome, codigo, preço))
  
def localize(): # Função para localizar o produto 
  
  if opcao == 2: # Caso se o usuáio escolher a opção 2
    localize = int(input('\nDigite o código do produto: '))
    print('\nO seu produto com o código de',localize,', foi localizado com sucesso!\n')

def edite(): #função para editar o produto

  if opcao == 3: # Caso se o usuário se escolher a opção 3
    edite = int(input('\nDigite o código do produto: '))
    print('\nO seu produto com o código de',edite,', foi editado com sucesso!\n')

def delete(): #Função para deletar um protudo

  if opcao == 4: #Caso o usuário escolher a opção 4
    detele = input('\nDigite o código do produto: ')
    print('\nProduto com o código de', detele,', foi excluido com sucesso!\n')

#Chamando as funções

cadastrar()
localize()
edite()
delete()
