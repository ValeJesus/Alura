
"""Encontra palavras em comum entre dois textos fornecidos pelo usuário.

O programa solicita dois textos, divide cada um em palavras (ignorando maiúsculas/minúsculas),
converte em conjuntos para remover duplicatas, e encontra a interseção
(palavras presentes em ambos os textos).
"""

# Solicita o primeiro texto, converte para minúsculas, divide em palavras e cria conjunto
texto1 = set(input('Escreva o texto 1 aqui: ').lower().split())

# Faz o mesmo para o segundo texto
texto2 = set(input('Escreva o texto 2 aqui: ').lower().split())

# Encontra palavras comuns a ambos os textos usando interseção
comuns = texto1.intersection(texto2)

# Exibe as palavras em comum
print(f"Palavras em comum: {comuns}")
 
