from ticketmaster_shows import get_shows
import functions
import PySimpleGUI as sg
import time


sg.theme("brightcolors")
clock = sg.Text("", key="clock", font=("Arial", 8))
label_1 = sg.Text(f"\n Click the button to see who's playing music in Seattle tonight\n")
label_2 = sg.Text("Press the button, dude.\n")
spacer = sg.Text("")
show_button = sg.Button("Show me the music!", size=40, mouseover_colors="LightBlue2", tooltip="Press it.", key="show")
list_box = sg.Listbox(values=[f"Press the Button....do it."], enable_events=True, size=(70,25), key="list")
exit_button = sg.Button("Exit")

window = sg.Window("Who's Playing in Seattle?",
                   layout=[[clock],
                           [label_1],
                           [label_2],
                           [show_button],
                           [spacer],
                           [list_box]],
                   element_justification='c',
                   font=('Helvetica', 13))


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))
    print(1, event)
    print(2, values)

    match event:
        case "show":
            window["list"].update(values=functions.print_shows(""))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()




