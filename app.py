from os import system,name
from transactionSheet import TransactionSheet
from transaction import Transaction
from tabulate import tabulate

menus = ['Nova Transação', 'Listar Transações', 'Total', 'Sair']
loop = 1
sheet = TransactionSheet()

def clear():
    system('cls' if name == 'nt' else 'clear')

def header():
    print('')
    print('')
    print('========== pyMoney - Gestor Financeiro em Python ==========')
    print('')

def menu():
    for i in range(len(menus)):
        print('{} - {}'.format(i + 1,menus[i]))
    
    print('')
    
    try:
        opcao = int(input('Informe uma opção: '))
    except:
        print('')
        print('Opção inválida!')
        input('Pressione enter para continuar...')
        print('')
        return
    
    if opcao == 1:
        newTransaction()
    elif opcao == 2:
        listTransactions()
    elif opcao == 3:
        showTotal()
    else:
        clear()
        
    return opcao

def newTransaction():
    clear()
    header()
    print('Nova Transação')
    print('')
    print('\033[0;34m')
    print('Tipos: E = Entrada e S = Saída')
    print('\033[0;97m')
    print('')
    
    transaction = Transaction()
    transaction.title = str(input('Título: '))
    transaction.value = str(input('Valor: ')).replace(",",".")
    transaction.type = str(input('Tipo: '))
    transaction.category = str(input('Categoria: '))
    sheet.add(transaction)
    
def listTransactions():
    clear()
    header()
    print('Lista de Transações')
    print('')
    lista = sheet.getAll()
    tableHeader = ["Título","Valor","Tipo","Categoria"]
    table = tabulate(lista, headers=tableHeader)
    print(table)
    print('')
    input('Pressione enter para voltar...')

def showTotal():
    newPage('Total')
    total = sheet.getTotal()
    table = tabulate(total['types'], headers=['Tipo','Valor'])
    print(table)
    print('')
    print('Saldo: ' + str(total['total']))
    print('')
    input('Pressione enter para voltar...')

def newPage(title):
    clear()
    header()
    print(title)
    print('')
while loop == 1:
    clear()
    header()
    if menu() == 4:
        loop = 0
        print('Done!')