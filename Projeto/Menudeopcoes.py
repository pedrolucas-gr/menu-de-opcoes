from time import sleep
print('========= \033[1;34mMENU DE OPÇÕES\033[m =========')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maior = opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa''')
    opcao = int(input('Qual operação você deseja realizar? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        else:
            print('Os números {} e {} são iguais'.format(n1, n2))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=' * 30)
    sleep(1)
print('Fim do programa!')
