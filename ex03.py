idade = int(input("Digite sua idade: "))
mesAtual = int(input("Mes de Atual: "))
mesNasc = int(input("Mes nascimento: "))

if mesNasc >= mesAtual:
    anoNascimento = 2023 - idade - 1
else:
    anoNascimento = 2023 - idade
print(anoNascimento)
