import random
from questions import questions

# Configurações do jogo
NUM_CASAS = 20

def main():
    print("Bem-vindo ao Desafio do Programador!")
    
    # Lógica para obter o número de jogadores e seus nomes
    num_jogadores = 0
    while num_jogadores < 2 or num_jogadores > 4:
        try:
            num_jogadores = int(input("Quantos jogadores (2-4)? "))
        except ValueError:
            print("Por favor, digite um número válido.")

    jogadores = []
    for i in range(num_jogadores):
        nome = input(f'Nome do Jogador {i+1}: ')
        jogadores.append({"nome": nome, "posicao": 0})

    print("\n--- Jogo Iniciado ---")
    
    # Loop principal do jogo
    jogador_atual_idx = 0
    while True:
        jogador_atual = jogadores[jogador_atual_idx]
        print("\nTurno de {}".format(jogador_atual["nome"]))
        print("Posição atual: {}".format(jogador_atual["posicao"]))

        input("Pressione Enter para lançar o dado...")
        dado = random.randint(1, 6)
        print(f"Dado: {dado}")

        posicao_anterior = jogador_atual["posicao"]
        nova_posicao = posicao_anterior + dado
        
        print(f"Você avançou para a casa {nova_posicao}.")

        # Lógica para perguntas e movimentação
        pergunta_aleatoria = random.choice(questions)
        print(f"\nPergunta da Casa {nova_posicao}:")
        print(pergunta_aleatoria["pergunta"])
        for i, opcao in enumerate(pergunta_aleatoria["opcoes"]):
            print(f"{i+1}. {opcao}")

        resposta_jogador = input("Sua resposta (digite o número da opção): ")
        
        try:
            resposta_idx = int(resposta_jogador) - 1
            if 0 <= resposta_idx < len(pergunta_aleatoria["opcoes"]):
                if pergunta_aleatoria["opcoes"][resposta_idx] == pergunta_aleatoria["resposta_correta"]:
                    print("Resposta correta! Você permanece na casa.")
                    jogador_atual["posicao"] = nova_posicao
                else:
                    print("Resposta incorreta. A resposta correta era: {}".format(pergunta_aleatoria["resposta_correta"]))
                    print("Você volta para a casa {}.".format(posicao_anterior))
                    jogador_atual["posicao"] = posicao_anterior
            else:
                print("Opção inválida. Você volta para a casa anterior.")
                jogador_atual["posicao"] = posicao_anterior
        except ValueError:
            print("Entrada inválida. Você volta para a casa anterior.")
            jogador_atual["posicao"] = posicao_anterior

        # Condição de vitória
        if nova_posicao >= NUM_CASAS - 1:
            print("Parabéns, {}! Você chegou ao final do tabuleiro e venceu o Desafio do Programador!".format(jogador_atual["nome"]))
            break

        jogador_atual["posicao"] = nova_posicao

        # Passar para o próximo jogador
        jogador_atual_idx = (jogador_atual_idx + 1) % num_jogadores

if __name__ == "__main__":
    main()


