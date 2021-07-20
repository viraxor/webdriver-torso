import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
from random import randint as rnd
from PIL import ImageGrab

root = tk.Tk()
figure = 0

root.title('Webdriver Torso')

canvas = tk.Canvas(root, width=820, height=550, bg="white")

color1 = "#ff0000"
color2 = "#0000ff"

def webdrivertorso(e=None):
    global figure
    figure += 1
    root.title('Webdriver Torso - Figure {figure}'.format(figure=figure))
    
    canvas.delete('all')
    a = canvas.create_rectangle(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill=color1)
    b = canvas.create_rectangle(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill=color2)

def savewebdrivertorso(e=None):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    
    ImageGrab.grab(bbox=(x, y, x1, y1)).save("figures/figure{figure}.png".format(figure=figure))

    messagebox.showinfo(title="Image saved", message="The image is successfully saved.")

def saveaswebdrivertorso(e=None):
    dialog = filedialog.asksaveasfilename(filetypes=(("PNG file", "*.png"), ("JPG file", "*.jpg")))
    if dialog:
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        if not (dialog.endswith(".png") or dialog.endswith(".jpg")):
            dialog += ".png"

        ImageGrab.grab(bbox=(x, y, x1, y1)).save(dialog)

    messagebox.showinfo(title="Image saved", message="The image is successfully saved.")

genbtn = tk.Button(root, command=webdrivertorso, text="Generate")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)

file_menu.add_command(label="Save", command=savewebdrivertorso)
file_menu.add_command(label="Save As...", command=saveaswebdrivertorso)

menubar.add_cascade(label="File", menu=file_menu)

def choosecolor(e=None):
    global color1, color2
    colordialog1 = colorchooser.askcolor()
    colordialog2 = colorchooser.askcolor()

    if colordialog1:
        color1 = colordialog1[1]
    if colordialog2:
        color2 = colordialog2[1]

    messagebox.showinfo(title="Colors changed", message="The rectangle colors are successfully changed.")

view_menu = tk.Menu(menubar)

view_menu.add_command(label="Change color...", command=choosecolor)

menubar.add_cascade(label="View", menu=view_menu)

canvas.grid(row=0, column=0)
genbtn.grid(row=1, column=0)

root.bind("<Control-n>", webdrivertorso)
root.bind("<Control-s>", savewebdrivertorso)
root.bind("<Control-S>", saveaswebdrivertorso)

webdrivertorso()

root.mainloop()
