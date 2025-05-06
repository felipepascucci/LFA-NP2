def pertence_linguagem(w):
    # Verifica se a string está na linguagem L = {a^n b^n | n >= 0}
    n = len(w)
    meio = n // 2
    return w[:meio] == 'a' * meio and w[meio:] == 'b' * meio and all(c in 'ab' for c in w)

def lema_do_bombeamento(w, p):
    print(f"Analisando cadeia: {w}, com p = {p}\n")
    encontrou_quebra = False

    for i in range(1, p + 1):
        x = w[:i-1]
        y = w[i-1:i]
        z = w[i:]
        print(f"Testando divisao: x='{x}', y='{y}', z='{z}'")
        
        for i_val in [0, 2]:
            w_bombeada = x + y * i_val + z
            pertence = pertence_linguagem(w_bombeada)
            status = "PERTENCE a L" if pertence else "NAO pertence a L"
            print(f"  Com i={i_val}: '{w_bombeada}' -> {status}")
            if not pertence:
                encontrou_quebra = True
        print()

    if encontrou_quebra:
        print("QUEBRA DO LEMA: A linguagem NAO é regular.")
    else:
        print("NAO houve quebra: O lema do bombeamento NAO prova que a linguagem é nao-regular.")

# Executar exemplo
w = "aaaabbbb"
p = 4
lema_do_bombeamento(w, p)
