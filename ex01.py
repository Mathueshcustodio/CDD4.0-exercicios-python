# 1- Faça um algoritimo que recaba 2 notas e calcule a media aritimetrica#
media = 0
nota1 = float(input("Digite a primeira Nota: "))
nota2 = float(input("Digite a segunda Nota: "))
media = (nota1 + nota2) / 2

if (media >= 7):
    print("Aprovado!")
elif (media >= 4):
    print("Recuperação!")
else:
    print("Reprovado.")

print("A media é {}".format(media))