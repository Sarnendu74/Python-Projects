# Initialize dictionary
team = {}

# Define a function for adding team player
def add_player(team):
    limit = int(input("How many players do you want to add? "))
    while len(team) < limit:
        name = input("Enter player name: ").capitalize()
        if name in team:
            print("Player already exists. Please enter a new player.")
            continue
        try:
            score = int(input("Enter player score: "))
        except ValueError:
            print("Invalid score. Please enter an integer value.")
            continue
        team[name] = score
        print(f'{name} added successfully.')
    print('All players added.')

# Define display function
def display(team):
    if not team:
        print("Empty Scoreboard. Please add some players and scores.")
    else:
        print("Team Scoreboard:")
        for key, value in team.items():
            print(f'Player: {key} | Score: {value}')

# Define update function
def update(team):
    if not team:
        print("No players to update.")
        return

    try:
        limit = int(input("How many scores do you want to update? "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return

    if limit <= 0:
        print("Enter a valid number of updates.")
        return
    if limit > len(team):
        print("Insufficient players to update according to the limit.")
        return

    for _ in range(limit):
        name = input("Enter player name to update: ").capitalize()
        if name not in team:
            print(f"Player {name} does not exist.")
            break
        try:
            score = int(input("Enter new score: "))
        except ValueError:
            print("Invalid score. Please enter an integer value.")
            continue
        team[name] = score
        print(f'Score for {name} updated successfully.')

# Define remove function
def remove(team):
    if not team:
        print("Player doesn't exist")
    else:
        try:
            name = str(input("Enter name: ").capitalize())
        except TypeError as e:
            print("Input should be a name.")
        del team[name]
        print(f'{name} removed successfully')
        

def main():
    while True:
        print("\n-----::: Team Management Menu :::-----")
        print("1. Add Player")
        print("2. Update Score")
        print("3. Remove Player")
        print("4. Display Team Board")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            add_player(team)
        elif choice == 2:
            update(team)
        elif choice == 3:
            remove(team)
        elif choice == 4:
            display(team)
        elif choice == 5:
            print("Thank you! for using our program. It's made by Sarnendu")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
