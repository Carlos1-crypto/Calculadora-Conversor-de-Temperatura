print("Bem Vindo à Calculadora Simples!!!!\n")

def calculadora():
    while True:
        print("1. Soma\n"
              "2. Subtração\n"
              "3. Multiplicação\n"
              "4. Divisão\n"
              "5. Sair\n")
        operacao = (input("Escolha a operação: "))
        try:
            operacao = int(operacao)
        except ValueError:
            print('Algo deu errado, digite apenas números inteiros.')
            continue

        if operacao in [1, 2, 3, 4, 5,]:
            em_funcionamento(operacao)
        else:
            print('Algo deu errado, digite apenas números inteiros.')

def soma(a=float, b=float):
    soma = a + b
    return soma

def subtracao(a=float, b=float):
    subtracao = a - b
    return subtracao

def multiplicacao(a=float, b=float):
    multiplicacao = a * b
    return multiplicacao

def divisao(a=float, b=float):
    if b != 0:
        divisao = a / b
        return divisao
    else:
        print("Divisão por zero não é permitida.")

def em_funcionamento(operacao):
    if operacao == 1:
        escolha = 'soma'
    elif operacao == 2:
        escolha = 'subtração'
    elif operacao == 3:
        escolha == 'multiplicação'
    elif operacao == 4:
        escolha = 'divisão'
    elif operacao == 5:
        print('Entendido. Antes de ir, você gostaria de usar o conversor de temperatura? (S/N)')
        resp = input('Resposta: ')
        if resp.isdigit():
            print('Algo deu errado, digite apenas sim ou não.')
            em_funcionamento(operacao=5)
        elif resp.isalpha():
            if resp in ['s', 'sim']:
                conversor_temperatura()
            elif resp in ['n', 'não', 'nao']:
                print('Ok, saindo...')
                exit()
            else:
                print('Algo deu errado, digite apenas sim ou não.')
                em_funcionamento(operacao=5)

    print(f"Você escolheu a operação {escolha}.\n"
          "Digite os números:")
    num1 = (input("Número 1: "))
    num2 = (input("Número 2: "))
    try:
        num1 = float(num1)
        num2 = float(num2)

    except ValueError:
        print('Algo deu errado, digite apenas números.')
        return em_funcionamento(operacao)

    if operacao == 1:
        print(f'Resultado: {soma(num1, num2)}\n')

    elif operacao == 2:
        print(f'Resultado: {subtracao(num1, num2)}\n')

    elif operacao == 3:
        print(f'Resultado: {multiplicacao(num1, num2)}\n')

    elif operacao == 4:
        print(f'Resultado: {divisao(num1, num2)}\n')

print("====Bem Vindo ao Conversor de Temperatura!====\n")

def conversor_temperatura():
    while True:
        print("1. Celsius para Fahrenheit\n"
              "2. Fahrenheit para Celsius\n"
              "3. Sair\n")

        escolha = (input("Escolha a opção: "))
        try:
            escolha = int(escolha)
        except ValueError:
            print('Algo deu errado, digite apenas números.')
            return conversor_temperatura()

        if escolha == 1:
            C_F()
        elif escolha == 2:
            F_C()
        elif escolha == 3:
            print('Saindo...')
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            conversor_temperatura()

def C_F():
    graus = (input("Digite a temperatura em Celsius: "))
    try:
        graus = float(graus)
    except ValueError:
        print('Algo deu errado, digite apenas números.')
        return C_F()
    Fahrenheit = (graus * 1.8) + 32
    return print(f'{graus} Graus Celsius em Fahrenheit é: {Fahrenheit} Graus Gahrenheit.')

def F_C():
    graus = (input("Digite a temperatura em Fahrenheit: "))
    try:
        graus = float(graus)
    except ValueError:
        print('Algo deu errado, digite apenas números.')
        return F_C()
    Celsius = (graus - 32) * 5 / 9
    return print(f'{graus} Graus Fahrenheit em Celsius é: {Celsius} Graus Celsius.')

calculadora()
