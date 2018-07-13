from Calculator_Construction import Calc_lib as Calc

repeat = "Y"
othercalc = "Y"
choicenum = 2
print("Welcome to the new command line app for finding the right concrete mixture!")
while othercalc == "Y" or othercalc == "y" and othercalc != "N" or othercalc != "n":
    print("What would you like to find?")
    print("Enter cement to find sand and aggregate(stones)? Type 1")
    print("Enter first sand to find cement and aggregate? Type 2")
    print("Enter aggregate to find cement and sand? Type 3")
    print("Or recommend you products? Type 4")
    choicenum = input()
    if choicenum == "1":
        Calc.cementtoall()
    elif choicenum == "2":
        Calc.sandtoall()
    elif choicenum == "3":
        Calc.aggregatetoall()
    elif choicenum == "4":
        Calc.recommend()
    else:
        print("\nI didn't understand you! Please enter a valid choice!\n")
        continue

    repeat = "Y"
    while repeat == "Y":
        othercalc = input("Would you like to do another calculation? (Y) for yes, (N) for no: ")
        if othercalc == "Y" or othercalc == "y" or othercalc == "N" or othercalc == "n":
            repeat = "N"
        else:
            print("I didn't understand you! Please enter a valid choice!")
            repeat = "Y"
