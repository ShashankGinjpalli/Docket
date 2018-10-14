

todo = []

f = open("todo.txt", "r+")
read = f.readlines()

for i in read:
    info = i
    x = info.split(",")
    todo.append([x[0],x[1]])

f.close()

while True:
    print("\n")
    print("1: Add events")
    print("2: Remove events")
    print("3: List events")
    print("4: Exit the Program")
    print("5: Clear Saved events")
    print("6: Clear Events in List")

    userInput = int(input("Please enter what you would like to do: \t"))

    if (userInput < 1 and  userInput> 6):
        print("Error: Please enter a valid menu option")
        userInput = int(input("Please enter what you would like to do: \t"))

    else:
        if(userInput == 1):
            name = str(raw_input("Enter the name of the todo: \t"))
            description = str(raw_input("Enter a description for the todo: \t"))
            todo.append([name,description])

        if(userInput == 2):
            removeIndex = int(input("Select Which Event # you would like to remove from the list:"))

            todo.remove(todo[removeIndex - 1])



        if(userInput == 3):
            print("\n")
            n = 0
            for i in todo:
                n = n+1
                print("Todo List event: \t" + str(n))
                print("name: \t\t\t\t" + i[0])
                print("description: \t\t" + i[1] + "\n")

            print("\n")

        if(userInput == 4):

            f = open("todo.txt", "w+")
            for i in todo:
                f.write(str(i[0]) +","+ str(i[1])+ "\n")

            f.close()

            exit()

        if(userInput == 5):
            f = open("todo.txt", "r+")
            f.truncate()
            f.close()
            print("Saved events have been Cleared")

        if(userInput == 6):
            while len(todo) > 0:
                todo.pop()