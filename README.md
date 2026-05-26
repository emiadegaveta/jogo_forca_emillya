# Jogo da Forca em Python 🎮

Este é um projeto interativo de **Jogo da Forca** desenvolvido em Python para rodar diretamente no terminal. O objetivo original do projeto era servir como base prática para estudantes de programação exercitarem lógica, manipulação de strings, listas e estruturas de repetição.

---

## 🚀 Como Jogar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou copie o código do arquivo principal (ex: `index.py`).
3. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python index.py

Escolha um tema, digite uma letra por rodada e tente adivinhar a palavra secreta antes que suas vidas acabem!

🛠️ Regras e Funcionamento
Vidas Iniciais: Você começa com 6 vidas.

Pontuação: * Acertar uma letra adiciona +10 pontos.

Errar uma letra desconta -2 pontos e remove 1 vida.

Validações: O sistema impede que você digite mais de uma letra por vez, números, caracteres especiais ou letras que já foram tentadas.

🎯 Missão dos Alunos (Concluída!)
O desafio proposto para a turma era evoluir o código inicial cumprindo dois objetivos:

Adicionar mais palavras ao repertório do jogo.

Categorizar por temas: Separar as palavras por categorias (como Jogos, Tecnologia, Escola, Filmes) e permitir que o jogador escolha o tema antes de começar.

🌟 Recursos Implementados:
Estrutura com Dicionário: Organização das palavras por chaves temáticas (banco_palavras).

Menu Dinâmico: O jogo agora lê os temas disponíveis e gera um menu numérico automaticamente para o usuário.

Novas Categorias: Inclusão de dezenas de palavras divididas entre Tecnologia, Jogos, Escola e Filmes.

📦 Tecnologias Utilizadas
Python 3 (Biblioteca padrão random, sem necessidade de instalações externas).
   
