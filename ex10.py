while True:
    num = int(input("Digite um numero : "))
    opcao = input("Qual a sua opção\n"
                  "1 para o antecessor\n"
                  "2 para o sucessor \n"
                  "3 para saio: ")
    if opcao == "1":
        print(num-1)
    elif opcao == "2":
        print(num+1)
    elif opcao == "3":
        break
    else:
        print("OPÇÃO INVALIDA!")