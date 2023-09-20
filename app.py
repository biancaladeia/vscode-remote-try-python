#importing the random module
import random

options = ['pedra', 'papel', 'tesoura'] #creating a list of options
score = 0 #initializing the score to 0
rounds_played = 0 #initializing the rounds played to 0

while True:
    random_choice = random.choice(options) # computador escolhe aleatoriamente
    player_choice = input("Escolha pedra, papel ou tesoura: ") # jogador escolhe

    #se o meu jogador escolher pedra
    if player_choice == 'pedra':
        rounds_played += 1

        if random_choice == 'pedra':
            print("Empate!")
        elif random_choice == 'papel':
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1

    #se o meu jogador escolher papel
    elif player_choice == 'papel':
        rounds_played += 1

        if random_choice == 'papel':
            print("Empate!")
        elif random_choice == 'tesoura':
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1

    #se o meu jogador escolher tesoura
    elif player_choice == 'tesoura':
        rounds_played += 1
        
        if random_choice == 'tesoura':
            print("Empate!")
        elif random_choice == 'pedra':
            print("Você perdeu!")
        else:
            print("Você ganhou!")
            score += 1
    
    #se o meu jogador escolher algo diferente de pedra papel e tesoura
    else:
        play_again = input("Quer jogar novamente? (s/n) ")
        if play_again == 's':
            continue
        elif play_again == 'n':
            print("Você ganhou", score, "vezes!")
            break

        else:
            print("Opção inválida!")
            break

