def pertence_linguagem(w):
    # exemplo: linguagem L = { a^n b^n | n ≥ 0 }, que NÃO é regular
    # a função retorna True se a palavra estiver na linguagem, senão False
    
    a_count = 0
    b_count = 0
    fase_b = False

    for c in w:
        if c == 'a':
            if fase_b:
                return False
            a_count += 1
        elif c == 'b':
            fase_b = True
            b_count += 1
        else:
            return False  # símbolo inválido

    return a_count == b_count


def aplicar_lema_bombeamento(pertence_linguagem, w, p):
    
    # aplica o lema do bombeamento na palavra w, com valor p
    # verifica se existe alguma divisão w = xyz que viole o lema 
    
    n = len(w)
    resultados = []

    if n < p:
        return "A cadeia é menor que p, o lema não se aplica!"

    for i in range(p + 1):  # |xy| <= p
        for j in range(i + 1, p + 1):  # |y| > 0
            x = w[:i]
            y = w[i:j]
            z = w[j:]

            print(f"\nDivisão: x='{x}', y='{y}', z='{z}'")
            violou = False
            for k in range(5):  # testar para i = 0 a 4
                nova_w = x + y * k + z
                resultado = pertence_linguagem(nova_w)
                print(f"Teste com i={k}: '{nova_w}' -> {'Pertence' if resultado else 'NÃO pertence'}")
                if not resultado:
                    violou = True

            if violou:
                return f"\nLema foi VIOLADO para a divisão x='{x}', y='{y}', z='{z}'\nPortanto, a linguagem NÃO é regular!"

    return "\nNenhuma violação encontrada. O lema se manteve para todas as divisões testadas!"

# exemplos de uso

# teste 1: Cadeia válida, número igual de 'a's e 'b's (n = 3)
# espera que o lema seja violado, pois a linguagem não é regular
w = "aaabbb"
p = 3
print("\nTeste 1: w = 'aaabbb', p = 3")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 2: Cadeia válida, número igual de 'a's e 'b's (n = 4)
# testa com uma palavra maior. O lema deve ser violado também
w = "aaaabbbb"
p = 4
print("\nTeste 2: w = 'aaaabbbb', p = 4")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 3: Cadeia inválida para a linguagem (2 'a's e 3 'b's)
# o lema não se aplica corretamente, pois w já não está em L
w = "aabbb"
p = 2
print("\nTeste 3: w = 'aabbb', p = 2")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 4: Cadeia com ordem intercalada (não está no formato a^n b^n)
# deve retornar False rapidamente em alguma repetição
w = "abab"
p = 2
print("\nTeste 4: w = 'abab', p = 2")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 5: Cadeia válida pequena, n = 1
# mesmo com cadeia curta, pode haver violação dependendo da divisão
w = "ab"
p = 1
print("\nTeste 5: w = 'ab', p = 1")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 6: Cadeia vazia (pertence à linguagem, pois n = 0)
# porém o lema não se aplica pois |w| < p
w = ""
p = 1
print("\nTeste 6: w = '', p = 1")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))

# teste 7: Cadeia válida com n = 5
# teste com cadeia maior, deve violar o lema também
w = "aaaaabbbbb"
p = 5
print("\nTeste 7: w = 'aaaaabbbbb', p = 5")
print(aplicar_lema_bombeamento(pertence_linguagem, w, p))