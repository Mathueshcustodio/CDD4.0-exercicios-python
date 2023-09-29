horaInicio = int(input("Digite a hora INICIAL do jogo: "))
horaFim = int(input("Digite a hora do FIM do jogo: "))

if horaInicio <= horaFim:
    duracao = horaFim - horaInicio
else:
    duracao = 24 - horaInicio + horaFim
print("A duração do jogo foi:{}".format(duracao))
