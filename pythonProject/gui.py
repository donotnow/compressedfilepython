# pypi.org
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip= "Enter a to-do")
add_button = PySimpleGUI.Button("Add", tooltip= "Add a to-do")

#window = PySimpleGUI.Window("My TD App", layout= [[label], [input_box]])
window = PySimpleGUI.Window("My TD App", layout= [[label], [input_box, add_button]])

window.read()
window.close()