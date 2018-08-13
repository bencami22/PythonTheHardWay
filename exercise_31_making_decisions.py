print("pick either door 1 or door 2")
door = input(">")

if door == "1":
    print("There s giant bear here eaiting a cheese cake. \n What do you do?\n 1. Take the cake \n2. Scream at the bear")
    bear = input(">")
    if bear == "1":
        print("Bear is angry")
    elif bear == "2":
        print("Bear is scared, and then angry again")
    else:
        print("good choice")
elif door == "2":
    print("You come across a sumo wrestler\nWhat do you do?\n1.punch him\n2.Kick him")
    punch_kick=input(">")

    if punch_kick == "1" or punch_kick == "2":
        print("He doesn't move")
    else:
        print("good choice")
else:
    print("cheater!")
