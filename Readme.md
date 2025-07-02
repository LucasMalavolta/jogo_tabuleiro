# Desafio do Programador - Jogo de Tabuleiro em Python

## Visão Geral

Este é um jogo de tabuleiro simples desenvolvido em Python, onde os jogadores testam seus conhecimentos em programação respondendo a perguntas. O objetivo é ser o primeiro a chegar ao final do tabuleiro.

## Requisitos do Projeto Final Atendidos

*   **Estrutura de Decisão/Condição**: Utilizada para verificar respostas, determinar movimentação (avançar/voltar) e condições de vitória.
*   **Laço de Repetição**: O jogo principal roda em um laço de repetição (`while True`) que continua até que um jogador vença. Laços `for` são usados para iterar sobre jogadores e opções de perguntas.
*   **Lista (necessário manuseá-la)**: Listas são usadas para armazenar os jogadores e suas informações, bem como para gerenciar as perguntas e suas opções.

## Como Jogar

1.  **Execução**: Execute o arquivo `main.py` em um terminal Python:
    ```bash
    python3 main.py
    ```
2.  **Número de Jogadores**: O jogo solicitará o número de jogadores (entre 2 e 4).
3.  **Nomes dos Jogadores**: Digite o nome de cada jogador quando solicitado.
4.  **Turnos**: Os jogadores se revezam. A cada turno, pressione Enter para lançar o dado.
5.  **Movimentação**: O jogador avança o número de casas indicado pelo dado.
6.  **Perguntas**: Ao cair em uma casa, uma pergunta de programação será apresentada com opções de resposta. Digite o número da opção correta.
    *   **Resposta Correta**: O jogador permanece na casa.
    *   **Resposta Incorreta**: O jogador volta para a posição que estava antes de lançar o dado.
7.  **Vitória**: O primeiro jogador a alcançar ou ultrapassar a casa final (casa 19) vence o jogo.

## Estrutura do Projeto

*   `main.py`: Contém a lógica principal do jogo, incluindo a interação com o usuário, movimentação dos jogadores, e verificação de respostas.
*   `questions.py`: Armazena a lista de perguntas e respostas do jogo. Cada pergunta é um dicionário com as chaves `pergunta`, `opcoes` e `resposta_correta`.

## Perguntas

As perguntas são sobre conceitos básicos de Python e programação. Você pode expandir o arquivo `questions.py` com mais perguntas para tornar o jogo mais desafiador e variado.

## Desenvolvimento

O jogo foi desenvolvido com foco na clareza do código e na implementação dos requisitos propostos. As saídas são baseadas em texto no console para simplicidade.


