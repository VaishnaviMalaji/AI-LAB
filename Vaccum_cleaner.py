
def vacuum_agent(location, status_A, status_B):
    if location == 'A' and status_A == 'Dirty':
        return 'SUCK'
    elif location == 'B' and status_B == 'Dirty':
        return 'SUCK'
    elif status_A == 'Dirty':
        return 'LEFT'
    elif status_B == 'Dirty':
        return 'RIGHT'
    else:
        return 'NO-OP'


def vacuum_simulation(location, status_A, status_B):
    print("\nInitial Environment:")
    print("Location:", location)
    print("Room A:", status_A)
    print("Room B:", status_B)
    print("\nAgent Actions:")

    while True:
        action = vacuum_agent(location, status_A, status_B)

        if action == 'NO-OP':
            print("Action: NO-OP")
            break

        if action == 'SUCK' and location == 'A':
            status_A = 'Clean'
        elif action == 'SUCK' and location == 'B':
            status_B = 'Clean'
        elif action == 'LEFT':
            location = 'A'
        elif action == 'RIGHT':
            location = 'B'

        print("Action:", action)
        print("Location:", location)
        print("Room A:", status_A)
        print("Room B:", status_B)
        print("-" * 25)

    print("\nFinal Environment State:")
    print("Final Location:", location)
    print("Room A:", status_A)
    print("Room B:", status_B)


# Get user input
location = input("Enter initial location (A/B): ").strip().upper()
status_A = input("Enter status of Room A (Clean/Dirty): ").strip().capitalize()
status_B = input("Enter status of Room B (Clean/Dirty): ").strip().capitalize()

# Validate input
if location not in ['A', 'B']:
    print("Invalid location! Enter A or B.")
elif status_A not in ['Clean', 'Dirty'] or status_B not in ['Clean', 'Dirty']:
    print("Invalid room status! Enter Clean or Dirty.")
else:
    vacuum_simulation(location, status_A, status_B)
