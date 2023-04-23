# Jogo do Dragão em Python

Este é um pequeno jogo em Python que simula um encontro com um dragão em uma floresta. O jogo é bastante simples e pode ser usado para fins educacionais ou para se divertir.

## Como Jogar

1. Abra um terminal ou prompt de comando.
2. Navegue até a pasta onde o arquivo do jogo está localizado.
3. Digite `python nome_do_arquivo.py` (substitua "nome_do_arquivo" pelo nome real do arquivo do jogo) e pressione Enter para iniciar o jogo.
4. Siga as instruções na tela para jogar o jogo.

## Funcionamento do Jogo

Quando o jogo começa, uma mensagem de introdução é exibida na tela, pedindo ao jogador que faça uma escolha: "a) Tenta correr e se esconder" ou "b) Enfrenta o dragão". O jogador deve digitar a letra correspondente à escolha desejada e pressionar Enter.

Se o jogador escolher "a", uma mensagem será exibida dizendo que ele conseguiu escapar. Se o jogador escolher "b", ele será solicitado a escolher uma arma para lutar contra o dragão, escolhendo entre "a) Espada", "b) Arco e flecha" ou "c) Machado".

Depois que o jogador escolhe a arma, o programa usa a função `random.choice()` para escolher aleatoriamente entre "vitória" ou "derrota". Se o resultado for "vitória", uma mensagem é exibida dizendo que o jogador derrotou o dragão. Se o resultado for "derrota", uma mensagem é exibida dizendo que o jogador foi derrotado pelo dragão.

Se o jogador digitar uma escolha inválida (qualquer coisa diferente de "a" ou "b" na primeira escolha ou qualquer coisa diferente de "a", "b" ou "c" na segunda escolha), uma mensagem de erro será exibida e o jogador será solicitado a escolher novamente.

Após a conclusão de cada rodada, o jogo perguntará ao jogador se ele deseja jogar novamente ou sair do jogo.
