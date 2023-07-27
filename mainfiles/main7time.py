from modules import function
import time
while True:
    datenow = time.strftime("%d-%m-%Y")
    timenow = time.strftime("%I:%M:%S")
    print(f"Date is {datenow}")
    print(f"Time is {timenow}")
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = function.get_file_todos()

        todos.append(todo + '\n')
        function.write_file_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):  # bitwise or operator
        todos = function.get_file_todos()
        for index, items in enumerate(todos):
            items = items.strip("\n")
            print(f"{index + 1}- {items}")
    elif user_action.startswith("edit"):
        try:
            todos = function.get_file_todos()
            number = int(user_action[5:])
            number = number - 1
            edited_todo = input(f"Replace {todos[number]} with : ")
            todos[number] = edited_todo + '\n'
            print(f"Replaced with {edited_todo}")
            function.write_file_todos(todos)
        except ValueError or IndexError:
            print("You entered an invalid command")
            continue

            # print(todos)
    elif user_action.startswith("complete"):
        try:
            todos = function.get_file_todos()
            number = int(user_action[9:])
            number = number - 1
            print(f"The Task {todos[number]} is completed :)")
            todos.pop(number)
            function.write_file_todos(todos)
        except IndexError or ValueError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("The command is not valid")

print("program ended")