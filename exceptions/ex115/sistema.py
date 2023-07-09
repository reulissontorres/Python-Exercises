from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastradar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar nova pessoas
        cabecalho('CADASTRO DE PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma resposta válida!\033[m')
    sleep(2)
