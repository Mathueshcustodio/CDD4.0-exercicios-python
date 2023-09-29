diasDeVida = 0
idade = int(input("Digite sua idade: "))
mes = int(input("Digite o Mês: "))
dias = int(input("Digite os dias: "))

idade = idade * 365
mes = mes * 30
diasDeVida = idade + mes + dias

print("Os dias são: {}".format(diasDeVida))