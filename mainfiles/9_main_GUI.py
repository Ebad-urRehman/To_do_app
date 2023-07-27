import PySimpleGUI as sg
import function
label = sg.Text("Write a new todo")
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')
# now key is todo for input value
add_button = sg.Button("Add")
window = sg.Window("MY To Do App",
                   layout = [[label], [input_box, add_button]],
                   font=('Helvetica', 13))
while True:
    event, values = window.read()
# now above line stores the data i.e. add button label and input in that variable in form of tuple
# the second item in the tuple is dictionary from which 1st item is key and other is value
# 1st var  store the 1st value of tuple and 2nd var values store the 2nd value of dictionary
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_file_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')
            function.write_file_todos(todos)
        
        case sg.WINDOW_CLOSED:
            break

window.close()
