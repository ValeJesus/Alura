nomes =  ['Rocho', 'Buso', 'Fernando']


print(nomes)
nome_errado = input('\nDigite o nome incorreto na lista :')
nome_correto = input('\nAgora digite o nome correto : ')

nomes[nome_errado] = nome_correto

print(f'\n Lista atualizada{nomes}')