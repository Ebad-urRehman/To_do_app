# this is frontend because it tells where the app is CLI or GUI
# function.py is backend because it's logic has nothing to do with CLI or GUI and it only use
# for logical processing
# the lists returning by functions module file can be used in both CLI and GUI
# pip always execute in terminal not in console
# Window is type in GUI just like string and lists
# python does not have Window datatype by default we import it by 3rd party libraries such as PySimpleGUI
# Window("title of window", layout)
import PySimpleGUI as sg
from mainfiles import function
label = sg.Text("Write a new todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("MY To Do App",
                   layout = [[label], [input_box, add_button]],
                   font=('Helvetica', 13))
# list of instances of textbox
# these lists can only except widgets(buttons, textbox, inputbox) not strings or integers etc
# items in one square bracket means all the items in a row
# items in multiple square bracket means all the items are in multiple rows
window.read()
# the code after read line executed when we press close and end program
# places window on the screen
window.close()
# shows a cross close button at top
