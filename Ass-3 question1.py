alone = input("Traveling alone? ")

if (age >= 60 or (gender == "female" and alone == "yes")) and tatkal == "no" and holiday == "no":
    print("Eligible")
else:
    print("Not Eligible")