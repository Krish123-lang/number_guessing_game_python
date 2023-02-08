import random
comp = random.randint(1, 10)
#print(comp) # Uncomment this if you want to cheat the computer 😁😁😁


try:
    i = 1
    while True:
        user_inp = int(input("Enter the number from 1 to 10: "))

        if user_inp == comp:
            print("*** You won ***")
            print(f"Congratulations! You did it in {i} attempts ")
            break
        else:
            print("Try again !!!")
            i += 1

except Exception as e:
    print(e)
