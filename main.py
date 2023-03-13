import random
import tkinter
from tkinter import *

# from PIL import ImageTk, Image

limit = False
window_open_call = False

root = Tk()
root.geometry("600x600")
root.title("Realistic Gamertag Generator")
icon = PhotoImage(file='imgbin_t-shirt-elliot-alderson-angela-moss-clothing-png.png')
root.iconphoto(True, icon)
root.config(background="black")

# img = ImageTk.PhotoImage(Image.open("imgbin_t-shirt-elliot-alderson-angela-moss-clothing-png.png"))
# img_label = Label(image=img)

#Shows text
label = tkinter.Label(root)
label.place(x=100, y=380, )
label.config(font=("Comic Sans", 30))
name_history = []


def namegeneration():
    global name_selection
    with open("csvconvertedfile.txt", "r") as file:
        username_list = file.read().splitlines()
        name_selection = random.choice(username_list)
        name_history.append(name_selection)
        #print(name_selection)
        label.config(text=name_selection)




def create_window():
    global limit
    global window_open_call
    global second_window

    if not limit:
        window_open_call = True
        limit = True
        second_window = Tk()
        second_window.title("History")
        second_window.geometry("1000x1000")
        second_window.config(background="black")

    def on_closing():
        global window_open_call
        global limit
        window_open_call = False
        limit = False
        second_window.destroy()

    second_window.protocol("WM_DELETE_WINDOW", on_closing)
    return second_window

def show_name_history():
    for i in name_history:
        print(i)



def history_button_commands():
    new_window = create_window()
    show_name_history()
    new_window.label = tkinter.Label(new_window)
    new_window.label.place(x=0,y=0)
    new_window.label.config(text=name_history,font=("Comic Sans", 30), fg= "black")


def copy():
    root.clipboard_clear()
    root.update()


#buttons
button = Button(root, text="generate new name", command=namegeneration, font=("Comic Sans", 30))
button.place(x=100, y=250)
history_button = Button(root, text="history", font=("Comic Sans", 15), command=history_button_commands, )
history_button.place(x=400, y=330)
copy = Button(root, text="Copy Gamertag", command=copy, font=("Comic Sans", 10))
copy.place(x=100, y=330)

root.mainloop()
