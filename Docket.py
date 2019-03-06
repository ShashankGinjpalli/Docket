#Shashank Ginjpalli

# Creating a List for the Agenda and the Calendar

todo = []
calendar = []

# function used to
def mainMenu():
    print("\n")
    print("1: Todolist Menu")
    print("2: Calendar Menu")
    print("3: Exit the Program")

    userInput = int(input("Please enter which Menu you would like to access: "))
    if(userInput == 1):
        todoList()
    if(userInput == 2):
        calendarEvent()
    if(userInput == 3):
        f = open("todo.txt", "w+")
        for i in todo:
            f.write(str(i[0]) +","+ str(i[1])+ "\n")
        f.close()

        f2 = open("calendar.txt", "w+")
        for i in calendar:
            f2.write(str(i[0]) + ","+ str(i[1]) +"," + str(i[2] + "\n"))
        f2.close()

        exit()

    else:
        print("Error enter a valid menu option")
        mainMenu()



def todoList():
    # repeats the menu until the user exits the program
    while True:
        print("\n")
        print("1: Add events")
        print("2: Remove events")
        print("3: List events")
        print("4: Exit the main menu \n")
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

                mainMenu()

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


def calendarEvent():
    while True:
        print("\n")
        print("1: Add Event to Calendar")
        print("2: Remove an event from the Calendar")
        print("3: List Events")
        print("4: Exit to Main Menu")

        userInput = int(input("Enter what you would like to do: "))

        while(userInput < 1 or userInput > 4):
            print("Error: Enter a valid Menu option!")
            userInput = int(input("Enter what you would like to do: "))

        if(userInput == 1):
            print("\n")
            title = str(input("Enter a Title for the Event: "))
            description = str(input("Enter a Description for the Event: "))
            date = str(input("Enter a Date for the Event: "))

            calendar.append([title, description, date])

        if(userInput == 2):
            print("\n")
            remove = str(input("Enter the Name of the Event that You would like to remove"))
            x = 0
            for i in calendar:
                if(remove == i[0]):
                    calendar.remove(x)
                    break
            x = x + 1

        if(userInput == 3):
            print("\n")

            for i in calendar:

                print("Name: \t\t\t\t" + i[0])
                print("Description: \t\t\t" + i[1] + "\n")
                print("Date: \t\t\t\t" + i[2] + "\n")

            print("\n")

        if(userInput == 4):
            mainMenu()





def main():

    # opens a file in order to read saved events
    f = open("todo.txt", "r+")
    read = f.readlines()
    f2 = open("calendar.txt","r+")
    readcal = f2.readlines()

    # splits the stored data at the comma so the program can distinguish between the name
    # and the description
    for i in read:
        info = i
        x = info.split(",")
        todo.append([(x[0]),x[1]])

    f.close()

    for i in readcal:
        x = i.split(",")
        calendar.append([x[0],x[1],x[2]])
    f2.close()

    mainMenu()

main()
