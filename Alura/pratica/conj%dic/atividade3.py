
"""Compara listas de compras de Laura e Ana, identificando itens comuns e exclusivos.

O programa solicita duas listas separadas por vírgulas, converte em conjuntos
para facilitar operações de interseção e diferença, e exibe:
- Itens presentes em ambas as listas
- Itens exclusivos de Laura
- Itens exclusivos de Ana
"""

# Solicita a lista de Laura, divide por vírgulas e converte para conjunto (remove duplicatas)
laura = set(input("Lista da Laura: ").split(", "))

# Solicita a lista de Ana, divide por vírgulas e converte para conjunto
ana = set(input("Lista da Ana: ").split(", "))

# Encontra itens comuns a ambas as listas usando interseção
comuns = laura.intersection(ana)

# Encontra itens exclusivos de Laura (presentes em laura mas não em ana)
exclusivos_laura = laura.difference(ana)

# Encontra itens exclusivos de Ana (presentes em ana mas não em laura)
exclusivos_ana = ana.difference(laura)

# Exibe os itens comuns
print(f"Itens em ambas as listas: {', '.join(comuns)}")

# Exibe os itens exclusivos de Laura
print(f"Itens exclusivos de Laura: {', '.join(exclusivos_laura)}")

# Exibe os itens exclusivos de Ana (corrigido o typo)
print(f"Itens exclusivos de Ana: {', '.join(exclusivos_ana)}")
 