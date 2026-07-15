from game.gamepkg.x_o import start_game
from src.calpkg.calculator import add
def main():
    print("Hello, World!")
   
    result = add(3, 5)
    print(f"The sum of 3 and  is: {result}")
if __name__ == "__main__":
    main()
    
    print(__name__)
    print("Starting XO Game...")
    start_game()