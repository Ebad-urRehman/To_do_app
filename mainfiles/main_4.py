# making app user freindly user can now input choices and commands in one line
# use of if else statments
# using list slicing operation
# replit.com online IDE (Can't build GUI or camera softwares
while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        with open("../todo.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        # by using with open method we can create an object easily by syntax while opening file and there is not
        # a need to close the file
        with open("../todo.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):  # bitwise or operator
        with open("../todo.txt", "r") as file:
            todos = file.readlines()
        for index, items in enumerate(todos):
            items = items.strip("\n")
            print(f"{index + 1}- {items}")
    elif user_action.startswith("edit"):
        try:
            with open("../todo.txt", "r") as file:
                todos = file.readlines()
            number = int(user_action[5:])
            number = number - 1
            edited_todo = input(f"Replace {todos[number]} with : ")
            todos[number] = edited_todo + '\n'
            print(f"Replaced with {edited_todo}")
            with open("../todo.txt", "w") as file:
                file.writelines(todos)
        except ValueError or IndexError:
            print("You entered an invalid command")
            continue

            # print(todos)
    elif user_action.startswith("complete"):
        try:
            with open("../todo.txt", "r") as file:
                todos = file.readlines()
            number = int(user_action[9:])
            number = number - 1
            print(f"The Task {todos[number]} is completed :)")
            todos.pop(number)
            with open("../todo.txt", "w") as file:
                file.writelines(todos)
        except IndexError or ValueError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("The command is not valid")
    # case _:
    #     print("Wrong Input : ")

print("program ended")



