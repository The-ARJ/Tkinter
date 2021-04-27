from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

win = Tk()
win.title("Dialogue Box")
win.iconbitmap("directory.ico")


def open():
    global my_image
    win.filename = filedialog.askopenfilename(initialdir="/Downloads", title="Select a file",
                                              filetypes=(("png files", "*.png"), ("all files", "*.*")))

    # sets the location of the selected image in the label
    my_label = Label(win, text=win.filename).pack()
    # image also gets displayed
    my_image = ImageTk.PhotoImage(Image.open(win.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(win, text="open File", command=open).pack()

# Vertical Slider
vertical = Scale(win, from_=0, to=200)
vertical.pack()
# Horizontal Slider
horizontal = Scale(win, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()


# my_lable = Label(root,text = horizontal.get().pack()

# Function Slide Created
def slide():
    my_label = Label(win, text=horizontal.get()).pack()
    win.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# Function called
my_btn = Button(win, text="Click Me", command=slide).pack()


def show():
    myLabel = Label(win, text=clicked.get()).pack()


clicked = StringVar()
clicked.set("Days")
drop = OptionMenu(win, clicked, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
drop.pack()
myButton = Button(win, text="Show Selection", command=show).pack()

win.mainloop()
