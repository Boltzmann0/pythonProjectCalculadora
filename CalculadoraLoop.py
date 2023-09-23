def calculadora():
    while True:
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print("Resultado da soma:", resultado)
            elif escolha == '2':
                resultado = num1 - num2
                print("Resultado da subtração:", resultado)
            elif escolha == '3':
                resultado = num1 * num2
                print("Resultado da multiplicação:", resultado)
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado da divisão:", resultado)
                else:
                    print("Erro: Divisão por zero!")
        else:
            print("Essa opção não existe. Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calculadora()
