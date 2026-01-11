# Lesson 15 - Tamagotchi

## Task 1: Define the Tamatgochi Class
- Start by creating a class called Tamagotchi.
- Add a constructor (__init__) to initialize:
    - name: The pet’s name.
    - hunger
    - energy
    - happiness
    - age: Starts at 0.
*What should each pet have as (attributes)?*

*What default values make sense for these attributes?* 


## Task 2: Add a Status Method
### Display the Pet’s Status
Write a status method to show:
- hunger
- energy
- happiness
- age

### Purpose:
- Keeps the player informed about their pet’s needs.

### Hints:
- Use print statements to format the output nicely.
- Make sure the method is called in the game loop.

## Task 3: Add Methods for Actions
### Add Methods for Pet Actions

### Add methods to manage the pet’s needs:
- feed(): 
    -Reduces hunger slightly but may reduce happiness.
- play(): 
    -Increases happiness but drains energy and increases hunger.
- sleep(): 
    -Restores energy but increases hunger significantly.

*What should each action do to the pet’s attributes?*

*How will you prevent values from becoming unrealistic (e.g., hunger going below 0)?*

*Think through the logic for each method, what will change?*


## Task 4: Handle Aging and Game Over

### Add Aging and Winning/Losing Conditions

### Write a grow_older method:
- Increase age by 1 every day.
- Slightly increase hunger and decrease happiness over time.

### Add win/lose conditions:
- Win: Age reaches 15.
- Lose: 
  - Hunger reaches 100, or
  - energy drops to 0, or 
  - happiness drops to 0.

*What happens to the pet if the player ignores it?*
*How can you track the pet’s progress or failure?*


## Task 5: Interactive Menu and Game Loop
### Build the Interactive Menu and Game Loop
- The game loop will prompt the user for actions:
  - 1 for Feed.
  - 2 for Play.
  - 3 for Sleep.
  - 4 to Quit.

- Based on the player’s input, call the appropriate method (feed, play, or sleep).

- After each action, call grow_older to age the pet and check for win/lose conditions.

- End the loop:
  - Exit the game if the player chooses "Quit" or if the game ends due to a win/lose condition

*Test the menu with one action at a time (e.g., only "Feed" first).*
*Gradually add more options and test win/lose conditions.*

## Task 6: Extend your Tamagotchi Game

### Bonus Challenge: Add New Features to Your Game
**Goal**: Enhance your Tamagotchi game with extra features to make it more interactive and fun!

### Challenge Ideas:
**New Attribute**: Add a health attribute to track your pet’s overall well-being.

**New Action**: Create a train method to improve a new attribute, like intelligence or fitness.

**Random Events**: Introduce random events (e.g., "Your pet found a snack!" or "Your pet feels tired").

**Custom Aging**: Change the growth rate or aging logic to reflect better care for the pet.

*Choose and implement a bonus feature.*