
import random 

def create_game()->int:
    """Escoge la puerta ganadora"""
    return random.randint(0, 2)

def play_change(n:int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    success = 0
    for _ in range(n):
        winner = create_game()
        initial_choice = random.randint(0, 2)
        possible_doors = [i for i in range(3) 
                          if i != winner and i != initial_choice]
        opened = random.choice(possible_doors)
        
        new_choice = [i for i in range(3) 
                      if i != initial_choice and i != opened][0]
        
        if new_choice == winner:
            success += 1
            
    return success / n

def play_stay(n:int = 1000)->float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    success = 0
    for _ in range(n):
        winner = create_game()
        initial_choice = random.randint(0, 2)
        
        if initial_choice == winner:
            success += 1
            
    return success / n

def main():
    success_change = play_change()
    success_stay   = play_stay()
    print(f"{success_change=} {success_stay=}")


if __name__ == "__main__":
    main()