
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0


def print_welcome():
    print("Welcome to the Adventure Game!")
    print("You can explore, fight enemies, and find treasure.")


def choose_action():
    print("Choose an action:")
    print("1. Explore")
    print("2. Check Inventory")
    print("3. Quit")
    choice = input("Enter number: ")
    return choice


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Enter your player's name: ")
        self.player = Player(player_name)
        self.enemies_defeated = 0

    def encounter_enemy(self):
        enemy = Enemy("Goblin", 30, 10)
        print(f"A wild {enemy.name} appears!")

        while enemy.is_alive() and self.player.is_alive():
            print(f"Your health: {self.player.health}")
            print(f"{enemy.name}'s health: {enemy.health}")
            action = input("Do you want to (1) Attack or (2) Run? ")
            if action == '1':
                enemy.take_damage(15)
                print(f"You hit the {enemy.name} for 15 damage!")
                if enemy.is_alive():
                    self.player.take_damage(enemy.damage)
                else:
                    print(f"You defeated the {enemy.name}!")
                    self.enemies_defeated += 1
                    self.player.add_item('Gold Coin')
            elif action == '2':
                print("You run away safely.")
                break
            else:
                print("Invalid action.")

    def explore(self):
        print("You explore the area...")
        import random
        if random.choice([True, False]):
            self.encounter_enemy()
        else:
            print("You find nothing interesting.")

    def play(self):
        print_welcome()
        while self.player.is_alive():
            choice = choose_action()
            if choice == '1':
                self.explore()
            elif choice == '2':
                self.player.show_inventory()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice.")

        if not self.player.is_alive():
            print("You died! Game over.")
            print(f"Enemies defeated: {self.enemies_defeated}")


if __name__ == "__main__":
    game = Game()
    game.play()
 
