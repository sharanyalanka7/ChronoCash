import time

money = 0
time_left = 60  # seconds of survival

print("Welcome to ChronoCash: Time is Money!")
print("Survive by earning money before time runs out.\n")

while time_left > 0:
    print(f"⏳ Time left: {time_left} seconds | 💰 Money: {money}")
    choice = input("Type 'work' to earn $10 or 'wait' to lose time: ")

    if choice.lower() == "work":
        money += 10
    elif choice.lower() == "wait":
        pass
    else:
        print("Invalid choice!")

    time_left -= 5  # every turn costs 5 seconds
    time.sleep(1)

print("\nGame Over!")
print(f"You survived with ${money}.")
