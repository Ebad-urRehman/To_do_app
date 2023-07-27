# that is a script
def get_file_todos(filepath="todo.txt"):
    """ Read a text file and returns
    the list of todo items"""
    with open(filepath, "r") as fileobject:
        func_todos = fileobject.readlines()
    return func_todos


def write_file_todos(todos_arg, filepath="todo.txt"):
    with open(filepath, "w") as func_file:
        func_file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")

# by default the value of name is main
# but when we run this script by another function it gives us the name of the current script
# if we run this file above if statement will execute
# if we run main file above if statement will not execute
