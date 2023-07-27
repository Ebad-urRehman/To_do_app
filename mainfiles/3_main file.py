# making code more better file io
# context manager method
while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo Task : ") + "\n"
            with open("todo.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)
            # by using with open method we can create an object easily by syntax while opening file and there is not
            # a need to close the file
            with open("todo.txt", "w") as file:
                file.writelines(todos)

        case 'show' | 'display':  # bitwise or operator
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            for index, items in enumerate(todos):
                items = items.strip("\n")
                print(f"{index + 1}- {items}")
        case 'edit':
            number = int(input("Enter a number of Todo to edit : "))
            number = number - 1
            edited_todo = input(f"Replace {todos[number]} with : ")
            todos[number] = edited_todo + '\n'
            print(f"Replaced with {edited_todo}")
            with open("todo.txt", "w") as file:
                file.writelines(todos)
            # print(todos)
        case 'complete':
            number = int(input("Enter a number of Todo that is completed : "))
            number = number - 1
            print(f"The Task {todos[number]} is completed :)")
            todos.pop(number)
            with open("todo.txt", "w") as file:
                file.writelines(todos)
        case 'exit':
            break
        case _:
            print("Wrong Input : ")

print("program ended")



