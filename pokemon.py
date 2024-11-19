import random
import os
import time

# Clear screen function
def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Pause for readability
def sleep(seconds):
    time.sleep(seconds)

# Dash display function
def dash(trainer1, trainer2, pokemon1, pokemon2):
    print(f"{trainer1} v. {trainer2}\n")
    print(f"{pokemon1} v. {pokemon2}")
    print("    \\o/           \\o/")

# Clear screen
cls()

# Get trainer and Pokémon names
print("---Terminal Pokémon---")
trainer1 = input("Enter the first trainer's name: ")
trainer2 = input("Enter the second trainer's name: ")
pokemon1 = input(f"Enter {trainer1}'s Pokémon name: ")
pokemon2 = input(f"Enter {trainer2}'s Pokémon name: ")

# Move list and random assignment
moves = ["Tackle", "Flamethrower", "Thunderbolt", "Water Gun", "Earthquake", "Hyper Beam", "Ice Beam", "Psychic", "Surf", "Sludge Bomb", "Dragon Claw", "Shadow Ball"]

pokemon1_powers = random.sample(moves, 3)
pokemon2_powers = random.sample(moves, 3)

# Display moves
cls()
print(f"{trainer1} v. {trainer2}")
sleep(1)
print(f"{pokemon1}'s moves: {', '.join(pokemon1_powers)}")
print(f"{pokemon2}'s moves: {', '.join(pokemon2_powers)}")
sleep(2)
print("MATCH BEGINS!")
cls()

# Initialize health and damage
pokemon1_health = 100
pokemon2_health = 100

# Assign random damage for each move
move_damage = {move: random.randint(10, 25) for move in moves}

# Function to choose a move
def choose_move(trainer, pokemon, available_moves):
    print(f"\n{trainer}, it's your turn! {pokemon}'s available moves:")
    for i, move in enumerate(available_moves, 1):
        print(f"{i}. {move}")
    
    while True:
        try:
            choice = int(input("Choose a move by entering the number: "))
            if 1 <= choice <= len(available_moves):
                return available_moves[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

# Main game loop
turn = 0
while pokemon1_health > 0 and pokemon2_health > 0:
    cls()
    dash(trainer1, trainer2, pokemon1, pokemon2)

    # Determine whose turn it is
    attacker, defender, attacker_health, defender_health, attacker_moves, defender_health_var = (
        (trainer1, trainer2, pokemon1_health, pokemon2_health, pokemon1_powers, "pokemon2_health")
        if turn % 2 == 0
        else (trainer2, trainer1, pokemon2_health, pokemon1_health, pokemon2_powers, "pokemon1_health")
    )

    # Trainer chooses move
    chosen_move = choose_move(attacker, pokemon1 if turn % 2 == 0 else pokemon2, attacker_moves)

    # Calculate damage
    damage = move_damage[chosen_move]

    print(f"\n{attacker}'s {pokemon1 if turn % 2 == 0 else pokemon2} used {chosen_move}! It dealt {damage} damage.")
    sleep(2)

    # Deduct health
    if turn % 2 == 0:
        pokemon2_health -= damage
    else:
        pokemon1_health -= damage

    # Display health
    print(f"\n{pokemon1} has {max(pokemon1_health, 0)} HP left.")
    print(f"{pokemon2} has {max(pokemon2_health, 0)} HP left.")
    sleep(2)

    # Increment turn
    turn += 1

# Determine winner
cls()
if pokemon1_health <= 0:
    print(f"{pokemon2} wins! {trainer2} is victorious!")
else:
    print(f"{pokemon1} wins! {trainer1} is the champion!")

