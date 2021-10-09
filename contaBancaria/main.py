from conta import Conta

#numero = int(input('Informe o valor numero da sua conta: '))
#titular = input('Informe o nome titular da conta: ')
#limite = float(input('Informe o limite da conta: '))

contaOrigem = Conta(452, 'pessoa', 5000);
contaDestino = Conta(231, 'Outra pessoa', 7000)

resp = input('Você deseja realizar um deposito: (s/n)')
if resp == 's':
    valor = float(input('Informe um valor a ser depositado: '))
    contaOrigem.deposito(valor)

resp = input('Você deseja realizar um saque: (s/n)')
if resp == 's':
    valor = float(input('Informe um valor a ser sacado: '))
    contaOrigem.saque(valor)

resp = input('Você deseja realizar uma tranfêrencia: (s/n)')
if resp == 's':
    valor = float(input('Informe um valor da tranfêrencia: '))
    contaOrigem.transferencia(contaDestino, valor)

contaOrigem.extrato()
contaDestino.extrato()
contaOrigem.saldo = 2000