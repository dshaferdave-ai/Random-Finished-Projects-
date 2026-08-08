#test
import random
import time

asked_value = int(input("Pick a random number from 1,20"))
cake = input("Whats you favorite flavor of cake? ")
value = random.randint(1, 10)

if value >= 0 and value <= 10:
    print("step one complete, starting step two")
    time.sleep(3)
    if len(cake) <= 10:
        print("step two complete, starting step three")
        time.sleep(3)
        if asked_value == 3:
            print(f"Test Complete, The number you chose is {asked_value}, The type of cake you chose is {cake}, and the random value is {value}")
        else:
            print("Test Failed")
    else:
        print("Test Failed")
else:
    print("Test Failed")