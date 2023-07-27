# there is a problem with previous program that is if we close the program the data will be deleted but we want to store it for future
# we use filing for that purpose
# todos = [] we didn't need this file any more

while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo Task : ") + "\n"
            file = open("../todo.txt", "r")
            todos = file.readlines()
            # inputting old todos in todos var in memory
            file.close()
            todos.append(todo)
            # adding new todos to it
            file = open("../todo.txt", "w")
            # opening in write mode
            file.writelines(todos)
            # withing the file with all todos new and old
            # above line take list as an argument
            file.close()
        case 'show' | 'display':  # bitwise or operator
            file = open("../todo.txt", "r")
            todos = file.readlines()
            # types of todos here is lists
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)
            # new_todos = [item.strip("\n") for item in todos]  # it can replace above few lines
            file.close()

            for index, items in enumerate(todos):
                items = items.strip("\n")
                print(f"{index + 1}- {items}")
        case 'edit':
            number = int(input("Enter a number of Todo to edit : "))
            number = number - 1
            edited_todo = input(f"Replace {todos[number]} with : ")
            todos[number] = edited_todo
            print(edited_todo)
            # print(todos)
        case 'complete':
            number = int(input("Enter a number of Todo that is completed : "))
            number = number - 1
            print(f"The Task {todos[number]} is completed :)")
            todos.pop(number)
        case 'exit':
            break
        case _:
            print("Wrong Input : ")

print("program ended")

# if we change the file directory by clicking refactor pycharm automatically adjust the directory if not we can do it
# manually
# Method of creating a new file at another directory
file = open(r"J:\Python Courses\[FreeCourseSite.com] Udemy - Python Mega Course Learn Python in 60 Days, "
            r"Build 20 Apps\0. Websites you may like\file.txt", 'w')

# file cannot be created in read mode
