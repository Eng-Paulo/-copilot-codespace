def main():
  
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    
    operacao = input("Digite a operação (+, -, *, /): ")

    # Realiza a operação e exibe o resultado
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = (abs(num1 - num2))
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()