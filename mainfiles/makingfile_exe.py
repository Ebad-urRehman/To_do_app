import PySimpleGUI as sg
import function
import time
import os
# sg.theme("DarkBlue2")
# creating a file if it doesnot exits

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

clock_time = sg.Text("", key='clock')
label = sg.Text("Write a new todo")
input_box = sg.InputText(tooltip="Enter todo", key='inputted_todo')
list_box = sg.Listbox(values=function.get_file_todos(), key = 'selected_todos',
                      enable_events=True, size = [45, 10])
add_button = sg.Button(size=[10,1], image_source="004 add.png",
                       pad=((32, 0), (0, 0)), mouseover_colors="LightGreen",
                       tooltip="Add Todo", key="Add",
                       button_color="LightBlue")
edit_button = sg.Button("Edit",
                        size=8 ,mouseover_colors="LightGreen",
                        tooltip="Edit todo",
                        )
complete_button = sg.Button(size=8, image_source="004 complete.png",
                            mouseover_colors="LightGreen",
                            tooltip="Mark Selected as complete", key="Complete")
exit_button = sg.Button("Exit", tooltip="Exit the program")
left_column_content = [[list_box]]
right_column_content = [[edit_button],
                        [complete_button]]
right_column = sg.Column(right_column_content)
left_column = sg.Column(left_column_content)
window = sg.Window("MY To Do App",
                   layout=[[clock_time],
                            [label], [input_box, add_button],
                           [left_column, right_column],
                           [exit_button]],
                   font=('Helvetica', 13))
while True:
    event, values = window.read(timeout=200)
    # time updated in every 200ms
    window["clock"].update(value=time.strftime("%d-%m-%Y  %I:%M:%S %p"))
    match event:
        case "Add":
            todos = function.get_file_todos()
            new_todo = values['inputted_todo']
            todos.append(new_todo + '\n')
            function.write_file_todos(todos)
            window['selected_todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['selected_todos'][0]
                new_todo = values["inputted_todo"]
                todos = function.get_file_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                function.write_file_todos(todos)
                window['selected_todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select the item First", font=('Helvetica', 13))
        case "Complete":
            try:
                todo_to_complete = values["selected_todos"][0]
                todos = function.get_file_todos()
                todos.remove(todo_to_complete)
                function.write_file_todos(todos)
                window['selected_todos'].update(values=todos)
                window['inputted_todo'].update(value='')
            except IndexError:
                sg.popup("Please Select the item First", font=('Helvetica', 13))
        case 'selected_todos':
            window['inputted_todo'].update(value=values['selected_todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break


window.close()
