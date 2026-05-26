import random

# MISSÃO DOS ALUNOS CUMPRIDA:
# Lista inicial de palavras separada por temas usando um dicionário
banco_palavras = {
    "tecnologia": [
        "python", "programacao", "sistema", "algoritmo", "teclado", 
        "internet", "computador", "desenvolvedor", "software", "terminal"
    ],
    "jogos": [
        "minecraft", "fortnite", "console", "controle", "pixel", 
        "estrategia", "aventura", "tabuleiro", "multiplayer", "plataforma"
    ],
    "escola": [
        "professor", "caderno", "biblioteca", "caneta", "recreio", 
        "geografia", "historia", "matematica", "estudante", "diretoria"
    ],
    "filmes": [
        "madacascar", "titanic", "moana", "anabelle", "sobrenatural", 
        "django", "", "carros", "barbie", "avioes"
    ]
}

def escolher_tema_e_palavra():
    """Permite ao usuário escolher o tema e retorna uma palavra aleatória dele."""
    print("Escolha um tema para jogar:")
    
    # Lista os temas disponíveis dinamicamente
    temas = list(banco_palavras.keys())
    for i, tema in enumerate(temas, 1):
        print(f"{i} - {tema.capitalize()}")
    
    while True:
        try:
            opcao = int(input("\nDigite o número do tema desejado: "))
            if 1 <= opcao <= len(temas):
                tema_escolhido = themes = themes = temas[opcao - 1]
                # Escolhe uma palavra aleatória dentro do tema escolhido
                palavra_secreta = random.choice(banco_palavras[tema_escolhido])
                return tema_escolhido, palavra_secreta
            else:
                print("Opção inválida! Escolha um número da lista.")
        except ValueError:
            print("Por favor, digite apenas números.")

def mostrar_palavra(palavra, letras_acertadas):
    """Mostra a palavra com as letras já acertadas."""
    resultado = ""

    for letra in palavra:
        if letra in letras_acertadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    return resultado

def jogar():
    print("=" * 40)
    print("        JOGO DA FORCA - PYTHON")
    print("=" * 40)
    
    # Modificação para pegar o tema e a palavra
    tema, palavra_secreta = escolher_tema_e_palavra()
    
    letras_acertadas = []
    letras_tentadas = []
    vidas = 6
    pontos = 0

    print("\n" + "=" * 40)
    print(f"TEMA ESCOLHIDO: {tema.upper()}")
    print("Descubra a palavra secreta!")
    print("Você tem", vidas, "vidas.")
    print("=" * 40 + "\n")

    while vidas > 0:
        print("Palavra:", mostrar_palavra(palavra_secreta, letras_acertadas))
        print("Letras já tentadas:", letras_tentadas)
        print("Vidas:", vidas)
        print("Pontos:", pontos)
        print("-" * 40)

        letra = input("Digite uma letra: ").lower()

        # Validação da entrada
        if len(letra) != 1:
            print("Digite apenas UMA letra.")
            print()
            continue

        if not letra.isalpha():
            print("Digite apenas letras.")
            print()
            continue

        if letra in letras_tentadas:
            print("Você já tentou essa letra.")
            print()
            continue

        letras_tentadas.append(letra)

        if letra in palavra_secreta:
            print("Boa! A letra existe na palavra.")
            print()
            letras_acertadas.append(letra)
            pontos += 3
        else:
            print("Ops! Essa letra não está na palavra.")
            print()
            vidas -= 1
            pontos -= 2

        # Verifica se o jogador venceu
        venceu = True

        for letra_da_palavra in palavra_secreta:
            if letra_da_palavra not in letras_acertadas:
                venceu = False

        if venceu:
            print("=" * 40)
            print("PARABÉNS! VOCÊ VENCEU!")
            print("A palavra era:", palavra_secreta)
            print("Pontuação final:", pontos)
            print("=" * 40)
            break

    if vidas == 0:
        print("=" * 40)
        print("FIM DE JOGO!")
        print("A palavra era:", palavra_secreta)
        print("Pontuação final:", pontos)
        print("=" * 40)

# Início do programa
jogar()