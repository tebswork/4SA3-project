#view file
option = input(""""Please select an option:
                    A - Mood Tracker 
                    B - Journal 
                    C - Planner 
               """)
print("Option selected is: " + option)

if option == "A": 
    print("How are you feeling today?")
    feeling = input(""""Please select: 
               A - Happy
               B - Sad 
            C - Sensitive 
                    """)
    if feeling == "A": 
        print("Yay, that's good :)")
        response = input("Would you like to list three things you're grateful for?")
        print("Please select Y for yes and N for no.")
        if response == "Y":
            #open journal option 
        #elif response == "N":
            print("Would you like to select another option?")

    elif feeling == "B":
        print("Aw, sorry to hear that.")
        print("Would you like to write out your thoughts?")
    elif feeling == "C": 
        print("Oh I see, that's not a fun sensation.")
        print("What would you like to do now?")

elif option == "B":
    def entry(log): 
        print("Please enter your journal entry in the space below:")
        log = input()
        print(log)
        return iter(input)

elif option == "C":
    print("What goals do you have for today?")
    goal = input()
    print(goal)
