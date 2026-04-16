nomes = []
i = 0

while i < 10:
   coleta = input (f'Digite o nome do voluntário (ou "sair" para encerrar): ')
   if coleta == 'sair':
      break
   else:
      nomes.append(coleta)

print(f'Voluntários registrados{nomes}')
    
