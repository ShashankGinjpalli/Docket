
# Creating a List for the Agenda
todo = []

# opens a file in order to read saved events
f = open("todo.txt", "r+")
read = f.readlines()

# splits the stored data at the comma so the program can distinguish between the name
# and the description
for i in read:
    info = i
    x = info.split(",")
    todo.append([(x[0]),x[1]])

f.close()

# repeats the menu until the user exits the program
while True:
    print("\n")
    print("1: Add events")
    print("2: Remove events")
    print("3: List events")
    print("4: Exit the Program \n")
    print("In order to clear saved elements you have to run both 5 and 6")
    print("5: Clear Saved events")
    print("6: Clear Events in List")

    userInput = int(input("Please enter what you would like to do: \t"))

    # makes sure that the value entered is a menu option
    if (userInput < 1 and  userInput> 6):
        print("Error: Please enter a valid menu option")
        userInput = int(input("Please enter what you would like to do: \t"))

    else:
        if(userInput == 1):
            name = str(input("Enter the name of the todo: \t"))
            description = str(input("Enter a description for the todo: \t"))
            # appending a list with the name and the description to the main list
            todo.append([name,description])

        if(userInput == 2):
            removeIndex = int(input("Select Which Event # you would like to remove from the list:"))

            # deleting the event from the todo list
            todo.remove(todo[removeIndex - 1])



        if(userInput == 3):
            print("\n")
            n = 0
            for i in todo:
                n = n+1
                print("Todo List event: \t" + str(n))
                print("Name: \t\t\t\t" + i[0])
                print("Description: \t\t" + i[1] + "\n")

            print("\n")

        #saving to the file before exiting the program
        if(userInput == 4):

            f = open("todo.txt", "w+")
            for i in todo:
                f.write(str(i[0]) +","+ str(i[1])+ "\n")

            f.close()

            exit()

        # deletes the list events that are stored in the file
        if(userInput == 5):
            f = open("todo.txt", "r+")
            f.truncate()
            f.close()
            print("Saved events have been Cleared")


        # clears the list during the program runtime
        if(userInput == 6):
            while len(todo) > 0:
                todo.pop()