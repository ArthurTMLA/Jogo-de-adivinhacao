from random import randint
from time import sleep
from colorama import Fore, Style, init

# Inicializa colorama para cores no terminal
init(autoreset=True)

# Configurações do jogo
RN = randint(0, 10)  # Número aleatório de 0 a 10
limite = 10  # Número máximo de tentativas
tentativas = 0

print(Fore.CYAN + "🎲 Bem-vindo ao Jogo de Adivinhação!")
print("Eu escolhi um número entre 0 e 10.")
print(f"Você tem {limite} tentativas para acertar. Boa sorte!\n")

while tentativas < limite:
    try:
        # Entrada do jogador
        palpite = int(input(Fore.CYAN + f"Tentativa {tentativas + 1}: "))

        # Validação de intervalo
        if palpite < 0 or palpite > 10:
            print(Fore.RED + "❌ Número inválido! Digite apenas de 0 a 10.\n")
            continue  # Não conta como tentativa

        tentativas += 1
        print("Processando...\n")
        sleep(0.5)

        # Verificação do palpite
        if palpite == RN:
            print(Fore.GREEN + f"🎉 Você acertou em {tentativas} tentativa(s)! Eu pensei em {RN}!")
            break
        elif palpite > RN:
            print(Fore.YELLOW + "Errou! Dica: O número que eu pensei é menor que esse.\n")
        else:
            print(Fore.YELLOW + "Errou! Dica: O número que eu pensei é maior que esse.\n")

    except ValueError:
        print(Fore.RED + "❌ Entrada inválida! Digite apenas números.\n")

else:
    print(Fore.RED + f"❌ Que pena! Você não acertou em {limite} tentativas.")
    print(Fore.CYAN + f"O número que eu pensei era {RN}.")

