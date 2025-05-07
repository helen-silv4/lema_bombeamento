# 📚 Verificação do Lema do Bombeamento

Este projeto tem como objetivo aplicar o **Lema do Bombeamento** para mostrar que uma determinada linguagem **não é regular**, utilizando Python.

---

## 🧠 O que o programa deve fazer?

1. Receber uma linguagem `L` definida por uma função Python (`pertence_linguagem(w)`)
2. Receber um valor `p` de bombeamento
3. Receber uma cadeia `w ∈ L`, com `|w| ≥ p`
4. Simular **todas as possíveis divisões** `w = xyz`, com:
   - `|xy| ≤ p`
   - `|y| > 0`
5. Para cada divisão, testar `x y^i z` para `i = 0, 1, 2, 3, ...`
6. Verificar se todas as cadeias bombeadas **pertencem à linguagem**
7. Se alguma **não** pertencer, então o lema é **violado** e a linguagem **não é regular**

---

## 📘 Linguagem Utilizada

**L = { aⁿbⁿ | n ≥ 0 }**

Todas as palavras com uma sequência de `n` letras `'a'` seguidas de `n` letras `'b'`.

> Essa linguagem é conhecida por não ser regular.

---

## ✅ Exemplo de uso

### Cadeia testada:
```python
w = "aaabbb"
p = 3