def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            resultado = 0
    else:
        print("Operação não reconhecida. Use 1 para soma, 2 para subtração, 3 para multiplicação, ou 4 para divisão.")
        resultado = 0
    return resultado

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
