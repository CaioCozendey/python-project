import random

chars  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*().,?0123456789"

number = input("Quantidade de senhas: ")
number = int(number)

lenght = input("Tamanho da senha: ")
lenght = int(lenght)

print('\nAqui estão suas senhas: ')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
