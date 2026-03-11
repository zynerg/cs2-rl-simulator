# main.py

import time

class Game:
    def __init__(self):
        self.running = True
        self.speed = 1.0

    def main_loop(self):
        while self.running:
            self.update_game_state()
            self.handle_user_input()
            time.sleep(1 / self.speed)  # Control the speed of the game loop

    def update_game_state(self):
        # Logic for updating the game state
        print("Game state updated.")

    def handle_user_input(self):
        # Handle user inputs, like toggling speed or opening the punishment menu
        command = input("Enter command (toggle_speed, punish, quit): ")
        if command == 'toggle_speed':
            self.toggle_speed()
        elif command == 'punish':
            self.open_punishment_menu()
        elif command == 'quit':
            self.quit_game()

    def toggle_speed(self):
        self.speed = 2.0 if self.speed == 1.0 else 1.0
        print(f"Speed set to {self.speed}x.")

    def open_punishment_menu(self):
        print("Punishment Menu:")
        punish_type = input("Choose a punishment type (timeout, warning): ")
        print(f"Punishment applied: {punish_type}")

    def quit_game(self):
        self.running = False
        print("Game terminated.")

if __name__ == '__main__':
    game = Game()
    game.main_loop()