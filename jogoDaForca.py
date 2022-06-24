def linha():
    print('-' * 30)


palavra_secreta = 'homelander'
palavra_digitadas = []
chances = 3
cnt = 0
linha()
print('JOGO DA FORCA PYTHON'.center(30))
print('\033[1;31mA dica é: A droga de um super\033[m')

while chances != 0:
    linha()
    letra = str(input('Pressione um símbolo: '))

    if letra in palavra_digitadas:
        print('Opa! esse símbolo já foi digitado.\nNão sera adcionado, mas você também não perdera pontos.')

    if len(letra) != 1:
        print(f'Não! \033[30m{letra}\033[m é invalido, você deve digitar apenas um símbolo!\n'
              f'Esse erro não será descontado de suas chances.')
        print()
    else:
        palavra_digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'\033[32mO simbolo está correto!\033[m')
    else:
        if len(letra) == 1:
            print(f'\033[31mNãooo! Você errou.\033[m\nVocê tem agora {chances - 1} chances.')
            print()
            chances -= 1
            palavra_digitadas.pop()

    palavra_chave = ''

    for c in palavra_secreta:
        if c in palavra_digitadas:
            palavra_chave += c
        else:
            palavra_chave += '*'

    num_ast = palavra_chave.count('*')
    strings_descobertos = len(palavra_chave) - num_ast

    if strings_descobertos == len(palavra_secreta) - 3:
        chute = input('Deseje tentar advinhar a palavra? [S/N]').upper().strip()[0]
        if chute != 'S' and 'N':
            while True:
                chute = input('Deseje tentar advinhar a palavra? [S/N]').upper().strip()[0]
                if chute == 'S' or chute == 'N':
                    break

        if chute == 'S':
            resposta_final = input('Qual seu palpite? Lembrando que se errar perde duas chances: ')
            if resposta_final == palavra_secreta:
                print(f'\033[32mParabéns! você ganhou! a palavra é {palavra_secreta}\033[m')
                break
            else:
                chances -= 2
                print(f'\033[31mNãooo! infelizmente a palavra está incorreta!\nVocê ainda tem {chances} chances\033[m')

    if palavra_chave == palavra_secreta:
        print(f'você ganhou, a palavra é {palavra_secreta}!')
        break
    else:
        print(f'A palavra secreta esta assim: {palavra_chave}')

if chances == 0:
    print('\033[31mGame Over, você perdeu!.\033[m')
