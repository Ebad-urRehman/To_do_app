import PySimpleGUI as sg
import os
sg.theme("LightBlue7")
label1 = sg.Text("Do you want to Compress or Extract")
compress_button = sg.Button("Compress Files", key="Compress",
                            tooltip="Select Multiple files to compress into one zip file",
                            size=(14, 3))

extract_button = sg.Button("Extract Files", key="Extract",
                           tooltip="Select a Zip file to extract into a Folder",
                           size=(14, 3))

exit_button = sg.Button("Exit", tooltip="Exit the Program",
                        key="Exit", size=(11, 2))

buttons_list = [[label1],
             [compress_button],
              [extract_button],
                [exit_button]]
def open_compressor():
    os.system("python compressorapp.py")


def open_extractor():
    os.system("python extractorapp.py")



main_window = sg.Window("Extracter and Compressor",
                     layout=[
                             [sg.VPush(), sg.Column(buttons_list, element_justification="c",vertical_alignment="c")]

                             ],
                        size=(260, 250))


while True:
    event, values = main_window.read()

    match event:
        case "Compress":
            open_compressor()
        case "Extract":
            open_extractor()
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
main_window.close