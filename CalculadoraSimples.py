def calcular():
    while True:
        resp = input(
'''Insira qual operação deseja realizar:
        Adição: [+]
        Subtração: [-]
        Divisão: [/]
        Multiplicação: [*]
: ''')
        if resp not in ('+', '-', '/', '*'):
            print('A operação deve ser um dos símbolos', end='\n\n')
        else:
            try:
                num1 = int(input('Insira qual o primeiro número da operação: '))
                num2 = int(input('Insira qual o segundo número da operação: '))
                if resp == ('+'):
                    print(f"O resultado da operação {num1} + {num2} é igual a: ", num1+num2, end='\n\n')
                elif resp == ('-'):
                    print(f"O resultado da operação {num1} - {num2} é igual a: ", num1-num2, end='\n\n')
                elif resp == ('/'):
                    print(f"O resultado da operação {num1} / {num2} é igual a: ", num1/num2, end='\n\n')
                elif resp ==('*'):
                    print(f"O resultado da operação {num1} * {num2} é igual a: " , num1*num2, end='\n\n')
                else:
                    print('Value Error')
                    quit()
                continuar = input(
'''Deseja realizar outra operação?
    Sim: [s]
    Não: [n]
: ''')
                if continuar == 's':
                    pass
                else:
                    print('Encerrando')
                    quit()
            except:
                print('Value Error')
calcular()
