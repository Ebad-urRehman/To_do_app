import PySimpleGUI as sg
import zip_creater
label1 = sg.Text("Select Files to compress:")
label2 = sg.Text("Select Destination Folder:")
input1 =sg.Input()
input2 =sg.Input()
choose_button1 = sg.FilesBrowse("Browse", key="files")
choose_button2 = sg.FolderBrowse("Browse", key="folder")
compress_button = sg.Button("Compress")
output_label =sg.Text(key="output", text_color="blue")
exit_button = sg.Button("Exit")
window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:

    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values['files'].split(";")
            folderpath = values['folder']
            zip_creater.make_archive(filepaths, folderpath)
            window["output"].update(value="Compression Completed Successfully")
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
window.read()
window.close()