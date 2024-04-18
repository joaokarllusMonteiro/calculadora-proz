def calculadora():
    while True:
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        escolha = input("Digite o número para a operação correspondente: ")
        
        if escolha == '0':
            print("Saindo do programa...")
            break
        elif escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            
            if escolha == '1':
                print(f"Resultado: {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe.")
            
# Chama a função calculadora
calculadora()
