class Tamagotchi:
    def __init__(self, name):
        # Initialize the pet's attributes
        self.name = name
        self.hunger = 50   # Hunger level (0 = full, 100 = starving)
        self.energy = 50   # Energy level (0 = exhausted, 100 = full of energy)
        self.happiness = 50  # Happiness level (0 = sad, 100 = very happy)
        self.age = 0       # Age in virtual days

    def status(self):
        # Display the current status of the pet
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Age: {self.age} days")
        print("-" * 30)

    def feed(self):
        # Feeding reduces hunger but may slightly reduce happiness
        print(f"\nYou fed {self.name}.")
        self.hunger = self.hunger - 15 
        self.energy = self.energy + 5  # Small energy boost
        self.happiness = self.happiness - 3  # Slight happiness drop

    def play(self):
        # Playing increases happiness but drains energy and increases hunger
        print(f"\nYou played with {self.name}.")
        self.happiness = self.happiness + 20
        self.energy = self.energy - 15
        self.hunger = self.hunger + 10

    def sleep(self):
        # Sleeping restores energy but increases hunger significantly
        print(f"\n{self.name} is sleeping.")
        self.energy = self.energy + 30
        self.hunger = self.hunger + 20

    def grow_older(self):
        # Simulate the passage of time
        print(f"\n{self.name} is growing older...")
        self.age += 1
        self.hunger = self.hunger + 5  # Hunger increases naturally over time
        self.happiness = self.happiness - 5  # Happiness decreases naturally

        # Check if hunger, energy, or happiness is out of balance
        if self.hunger >= 100:
            print(f"\nOh no! {self.name} starved. Game over!")
            return True  # Game over due to starvation
        if self.energy <= 0:
            print(f"\nOh no! {self.name} collapsed from exhaustion. Game over!")
            return True  # Game over due to exhaustion
        if self.happiness <= 0:
            print(f"\nOh no! {self.name} is too sad to continue. Game over!")
            return True  # Game over due to unhappiness

        # Check for win condition
        if self.age >= 15:
            print(f"\nCongratulations! {self.name} has grown up healthy! You win!")
            return True  # Pet has grown up successfully
        return False

def main():
    # Introduction
    print("Welcome to the Tamagotchi Game!")
    pet_name = input("What is your Tamagotchi's name? ")
    pet = Tamagotchi(pet_name)

    print(f"\nSay hello to {pet_name}!")
    while True:
        # Show the pet's current status
        pet.status()

        # Prompt the user for an action
        print("\nWhat would you like to do?")
        print("1. Feed") #(reduces hunger slightly)
        print("2. Play") # (increases happiness, drains energy, raises hunger)
        print("3. Sleep") # (restores energy, increases hunger significantly)
        print("4. Quit")
        choice = input("Enter your choice: ")

        # Perform the corresponding action
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice. Please try again.")

        # Check if the pet has grown up or failed
        if pet.grow_older():
            break

# Run the game
# this code will only run when run directly.
# it will not run when imported as a module. 
# prevents accidental execution when other coders import this file
if __name__ == "__main__":
    main()
