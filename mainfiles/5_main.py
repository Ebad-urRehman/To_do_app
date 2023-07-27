# custom functions
# variable scope # variable defined in functions can't used outside that function
# ''' multiline strings
#  or comments called as strings for functions or string documentation '''
# they have \n by default at every new line if we don't want just add a \ (also add a single double quote at start and
# end with a \ at start
# if we place arguments wrong than parameters we can make it valid by adding a (parameter = argument) syntax

# take old todos from the file
def get_file_todos(filepath="todo.txt"):
    """ Read a text file and returns
    the list of todo items"""
    with open(filepath, "r") as fileobject:
        func_todos = fileobject.readlines()
    return func_todos


def write_file_todos(todos_arg, filepath="todo.txt"):
    with open(filepath, "w") as func_file:
        func_file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_file_todos()

        todos.append(todo + '\n')
        write_file_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):  # bitwise or operator
        todos = get_file_todos()
        for index, items in enumerate(todos):
            items = items.strip("\n")
            print(f"{index + 1}- {items}")
    elif user_action.startswith("edit"):
        try:
            todos = get_file_todos()
            number = int(user_action[5:])
            number = number - 1
            edited_todo = input(f"Replace {todos[number]} with : ")
            todos[number] = edited_todo + '\n'
            print(f"Replaced with {edited_todo}")
            write_file_todos(todos)
        except ValueError or IndexError:
            print("You entered an invalid command")
            continue

            # print(todos)
    elif user_action.startswith("complete"):
        try:
            todos = get_file_todos()
            number = int(user_action[9:])
            number = number - 1
            print(f"The Task {todos[number]} is completed :)")
            todos.pop(number)
            write_file_todos(todos)
        except IndexError or ValueError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("The command is not valid")

print("program ended")
