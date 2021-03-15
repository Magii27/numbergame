import random

print("Welcome to the NumberGame!")

var_try = 2
while var_try == 2:

    var_try = 1
    while var_try == 1:

        try:
            var_range1 = int(input("Choose your first number \n"))
            var_range2 = int(input("Choose your last number \n"))

            if (var_range2 - var_range1) < 9:
                print("Please choose a bigger range!")
                var_try = 1
            else:
                var_start = var_range1
                var_end = var_range2
                zahl = random.randrange(var_start, var_end)
                var_try = 0
        except ValueError:
            print("Please use numbers")
            var_try = 1

    var_try = 1
    while var_try == 1:

        try:
            var_zahl = int(input("Guess: \n"))

            if var_zahl < var_start or var_zahl > var_end:
                print("Use the range!")
            elif var_zahl > zahl:
                var_end = var_zahl
                print("Your number is lower than", var_zahl)
                print("New Range: ", var_start, " - ", var_end)
            elif var_zahl < zahl:
                var_start = var_zahl
                print("Your number is bigger than", var_zahl)
                print("New Range: ", var_start, " - ", var_end)
            else:
                print("You got it! The number you searched for is: ", zahl)
                print("GG")
                var_try = 0
        except ValueError:
            print("Please use numbers")
            var_try = 1

    while var_try == 0:

        var = input("New Game (n) - End (e) \n")

        if var == "n" or var == "N":
            var_try = 2
        elif var == "e" or var == "E":
            print("Goodbye!")
            var_try = 4
        else:
            print("I didnt understand this")