import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()
    
    if not user_option in options:
        print("Esa opción no es valida.")
        #continue
        return None, None
    
    computer_option = random.choice(options)

    print("User option => ", user_option)
    print("Computer option => ", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate! Se agrega un round más.")
        #rounds -= 1
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("User ganó!")
            user_wins += 1
        else:
            print("papel gana a piedra")
            print("Computer ganó!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "tijera":
            print("tijera gana a papel")
            print("Computer ganó!")
            computer_wins += 1
        else:
            print("papel gana a piedra")
            print("User ganó!")
            user_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("User ganó!")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("Computer ganó!")
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    rounds = 1
    user_wins = 0
    computer_wins = 0

    while True:
        
        print("*" * 20)
        print(f"..:: ROUND {rounds} ::..")
        print("*" * 20)

        print(f"El resultado actual es: Computer => {computer_wins} y User => {user_wins}")
    
        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)  
        
        if computer_wins == 2:
            print("Computer es el ganador general.")
            break

        if user_wins == 2:
            ("User es el ganador general.")
            break
            
        rounds += 1
    
run_game()
"""
def run_winner():

    user_wins, computer_wins = run_game() 

    if computer_wins == 2:
        print("Computer es el ganador general.")

    if user_wins == 2:
        ("User es el ganador general.")

run_game()
"""

"""
if rounds == 3: 
  if user > computer:
    print("User es el ganador general")
  else: 
    print("Computer es el ganador general")
"""
