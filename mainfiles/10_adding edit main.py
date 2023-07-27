import PySimpleGUI as sg
import function

label = sg.Text("Write a new todo")
input_box = sg.InputText(tooltip="Enter todo", key='inputted_todo')
list_box = sg.Listbox(values=function.get_file_todos(), key = 'selected_todos',
                      enable_events=True, size = [45, 10])
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
window = sg.Window("MY To Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 13))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_file_todos()
            new_todo = values['inputted_todo']
            todos.append(new_todo + '\n')
            function.write_file_todos(todos)
            window['selected_todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['selected_todos'][0]
            new_todo = values["inputted_todo"]
            todos = function.get_file_todos()
            index = todos.index(todo_to_edit)
            # finding index of todo_to_edit
            todos[index] = new_todo + '\n'
            function.write_file_todos(todos)
            window['selected_todos'].update(values=todos)
            # in above line the selected todo is updated with new todos object file
        case 'selected_todos':
            window['inputted_todo'].update(value=values['selected_todos'][0])
        case sg.WINDOW_CLOSED:
            break
            # if we added exit() the program ended here

window.close()
