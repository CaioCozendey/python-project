# Pedra Papel Tesoura...

import random

def play():
    user = input("Pedra Papel Tesoura... ")
    computer = random.choice(["pedra", "papel", "tesoura"])  
    print(computer)
    
    if user == computer:
        return "É um empate!"
    
    if win(user, computer):
        return "Você ganhou!"
    
    return "Você Perdeu"
    
    
def win(player, opponent):
    if(player == "pedra" and opponent == "tesoura") or (player == "tesoura" and opponent == "papel") or (player == "papel" and opponent == "pedra"):
        return True
    
print(play())