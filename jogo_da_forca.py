# Jogo da forca

secreto = 'perfume'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu todas as tentativas!!\n')
        break
    letra = input('Digite uma letra:\n')

    if len(letra) > 1:
        print('Digite apenas uma letra.\n')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra!!\n')
    else:
        print(f'A letra {letra} não existe na palavra!!\n')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Você ganhou, a palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()