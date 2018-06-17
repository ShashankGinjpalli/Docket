


todo = []

while True:
    print("\n")
    print("1: Add events")
    print("2: Remove events")
    print("3: List events")
    print("4: Exit the Program")

    userInput = int(input("Please enter what you would like to do: \t"))

    if (userInput < 1 and  userInput> 4):
        print("Error: Please enter a valid menu option")
        userInput = int(input("Please enter what you would like to do: \t"))

    else:
        if(userInput == 1):
            name = str(raw_input("Enter the name of the todo: \t"))
            description = str(raw_input("Enter a description for the todo: \t"))
            todo.append([name,description])

        if(userInput == 3):
            print("\n")
            for i in todo:
                print(i)

            print("\n")