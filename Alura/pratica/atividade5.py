import random

caracteres = [
' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
'0','1','2','3','4','5','6','7','8','9',
':', ';', '<', '=', '>', '?', '@',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'[','\\',']','^','_','`',
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'{','|','}','~'
]

while True:

    senha = ''.join(random.choice(caracteres) for _ in range(12))

    if (any(c.isupper() for c in senha) and
        any(c.islower() for c in senha) and
        any(c.isdigit() for c in senha) and
        any(not c.isalnum() for c in senha)):
        break

print("Senha:", senha)