#Crie um codigo que leia um numero diferente de zero e diga se este numero
#é positivo ou negativo#
sS = str
nN = str

resp = 's'
while resp == "s" or "S":
    numero = float(input("Digite um Numero: "))

    while numero == 0:
        numero = float(input("Digite Novamente: "))
    if numero > 0:
        print("O numero é positivo!")
    else:
       print("O numero é negativo")

    resp = str(input("Quer Digitar novamente ? s ou n ?"))