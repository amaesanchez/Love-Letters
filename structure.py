import random

InventoryToHer = []
InventoryToHim = []

# hello world
Intro = str(input("Who are you?: "))
for turn in range(2000000):
  if Intro == "Arlaine" or "arlaine":
    Prompt = str(input("Would you like to add a compliment or receive?: "))
    if Prompt == "add":
      InventoryToHim.append(str(input("What would you like to tell them?: ")))
    # problem: will keep looping under given name, wont prompt intro again for other user
    elif Prompt == "receive":
      print(random.choice(InventoryToHer))
    else:
      print("I'm sorry, I didn't catch that")
  elif Intro == "Eric" or "eric":
    Prompt = str(input("Would you like to add a compliment or receive?: "))
    if Prompt == "add":
      InventoryToHer.append(str(input("What would you like to tell them?: ")))
    elif Prompt == "receive":
      print(random.choice(InventoryToHim))
    else:
      print("I'm sorry, I didn't catch that")
