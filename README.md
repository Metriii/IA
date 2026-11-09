# atividade-nim

Atividades de Inteligência Artificial (CS50 AI) — implementações em Python.

## Conteúdo

- `atividade/` — **Nim com Q-learning**
  - `nim.py` — implementação das funções de Q-learning (`get_q_value`,
    `update_q_value`, `best_future_reward` e `choose_action`)
  - `play.py` — treina a IA em 10.000 partidas e permite jogar contra ela
  - `test_nim.py` — testes de progresso locais
  - `instrucoes.md` — enunciado da atividade
- `cesmac-ia/` — exercícios de aula (resolvedor de labirinto)
- `jogo_da_velha/` — atividades de Tic-Tac-Toe e Minesweeper
- `teste.html` — página de teste

## Como executar

### Nim

```bash
cd atividade
python test_nim.py     # roda os testes locais
python play.py         # treina a IA e abre uma partida contra ela
```

### Tic-Tac-Toe e Minesweeper

```bash
cd jogo_da_velha/cesmac-ia/atividade01/tictactoe
python runner.py

cd jogo_da_velha/cesmac-ia/atividade02/minesweeper
python runner.py
```

Requer Python 3.12+ (testado com Python 3.14).
