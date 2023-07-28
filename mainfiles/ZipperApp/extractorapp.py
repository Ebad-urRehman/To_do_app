import PySimpleGUI as sg
import zipextracter
label1 = sg.Text("Select a Zip File")
label2 = sg.Text("Extract to Location")
input1 = sg.Input()
input2 = sg.Input()
button1 = sg.FileBrowse("Browse", key="archive")
button2 =sg.FolderBrowse("Browse", key="folder")
extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output", text_color="Blue")

window = sg.Window("Archive Extracter",
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [extract_button, exit_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Extract":
            archive_path = values["archive"]
            dest_folder = values["folder"]
            zipextracter.extract_archive(archive_path, dest_folder)
            window["output"].update(value="Extraction Completed Successfully!")
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.close()