brancos = int(input("Digite os Votos Brancos: "))
nulos = int(input("Digite os Votos nulos: "))
validos = int(input("Digite os Votos validos: "))

total = (brancos + nulos + validos)
pocentual = (brancos / total) * 100
nulos = (nulos / total) * 100
validos = (validos / total) * 100


print("O numero total de brancos é: {:.2f}".format(pocentual))
print("O numero total de nulos é: {:.2f}".format(nulos))
print("O numero total de validos é: {:.2f}".format(validos))