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

# Exemplo de uso
w = "aaabbb"
p = 3
resultado = aplicar_lema_bombeamento(pertence_linguagem, w, p)
print(resultado)