# Task6 -Question 4: Unique Voters Registration
# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.
try:
    print("Welcome to INEC registration exercise")
    voters_bio = set()
    # name = set()
    for i in range(1,6):
        name = input(f"Enter name of voter {i} : ")
        if name not in voters_bio:
            voters_bio.add(name)
        else: 
            print("Name already exist")
    print("\nRegistration Completed.")
    print(f"Total Unique Voters Registered: {len(voters_bio)}")
    print("List of Voters:", voters_bio)
except ValueError:
            print("⚠ Invalid age. Please enter a name.")