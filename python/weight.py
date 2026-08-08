unknown = int(input("Weight : "))
unit = str(input("(K)g or (L)bs: "))

if unit == ("l" or "L"):
    final = unknown * 0.45392
    print("you weight in kgs is " , round(final))
elif unit == ("k" or "K"):
    final = unknown * 2.20462
    print("you weight in lbs is ",round(final))
else:
    print("ERROR")