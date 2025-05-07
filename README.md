## 📚 Verificação do Lema do Bombeamento

Este projeto tem como objetivo aplicar o **Lema do Bombeamento** para mostrar que uma determinada linguagem **não é regular**, utilizando Python.

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

## 📘 Linguagem Utilizada

**L = { aⁿbⁿ | n ≥ 0 }**

Todas as palavras com uma sequência de `n` letras `'a'` seguidas de `n` letras `'b'`.

> Essa linguagem é conhecida por não ser regular.

## ✅ Exemplo de uso

### 🧪 Testes

Foram realizados os seguintes testes com a linguagem **L = { aⁿbⁿ | n ≥ 0 }**:

| Nº | Cadeia (`w`)       | p  | Resultado Esperado                    | Observação                                    |
|----|---------------------|----|----------------------------------------|------------------------------------------------|
| 1  | `aaabbb`            | 3  | ❌ Viola o lema                        | Linguagem não é regular                       |
| 2  | `aaaabbbb`          | 4  | ❌ Viola o lema                        | Maior n, mesma violação                       |
| 3  | `aabbb`             | 2  | ✅ Já fora da linguagem                | Serve como reforço de comportamento           |
| 4  | `abab`              | 2  | ✅ Não pertence à linguagem            | Ordem alternada, fora da linguagem            |
| 5  | `ab`                | 1  | ❌ Viola o lema                        | Curta mas válida, lema ainda se aplica        |
| 6  | `""` (vazia)        | 1  | ✅ Não aplica o lema (|w| < p)         | Cadeia muito curta, não testada               |
| 7  | `aaaaabbbbb`        | 5  | ❌ Viola o lema                        | Reforça padrão: lema é sempre violado         |
