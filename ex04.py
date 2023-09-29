numero1 = int(input("Digite o numero1: "))
numero2 = int(input("Digite o numero2: "))
numero3 = int(input("Digite o numero3: "))

if (numero1 > numero3):
    print("O {} é maior".format(numero1))
elif (numero2 < numero3):
    print("O numero maior é{}".format(numero3))
else:
    print("O numero maior é {}".format(numero2))
