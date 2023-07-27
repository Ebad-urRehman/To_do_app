import PySimpleGUI as sg
from mainfiles import zip_creater
label1 = sg.Text("Select Files to compress:")
label2 = sg.Text("Select Destination Folder:")
input1 =sg.Input()
input2 =sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
output_label =sg.Text(key="output", text_color="blue")
window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(";")
    folderpath = values['folder']
    zip_creater.make_archive(filepaths, folderpath)
    window["output"].update(value="Compression Completed Successfully")
window.read()
window.close()