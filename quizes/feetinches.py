import PySimpleGUI as sg
label1 = sg.Text("Enter feet:")
label2 = sg.Text("Enter inches:")
input_box1 = sg.InputText(key="feet")
input_box2 = sg.InputText(key="inches")
convert_button = sg.Button("Convert Into Meters")
output_label = sg.Text(key="output", text_color="blue")
window = sg.Window("Feet and Inches to Meter Converter", layout=[[label1, input_box1],
                                                                [label2, input_box2],
                                                                [convert_button, output_label]], font=('Helvetica', 13))
while True:
    event, values = window.read()
    print(event)
    print(values)
    feet = int(values["feet"])
    inches = int(values["inches"])
    meters = feet * 0.3048 + inches/12 * 0.3048
    window["output"].update(value=str(meters) + " m")

window.read()
window.close()
