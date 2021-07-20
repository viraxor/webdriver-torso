import tkinter as tk
from tkinter import messagebox, filedialog
from random import randint as rnd
from PIL import ImageGrab

root = tk.Tk()
figure = 0

root.title('Webdriver Torso')

canvas = tk.Canvas(root, width=820, height=550, bg="white")

def webdrivertorso(e=None):
    global figure
    figure += 1
    root.title('Webdriver Torso - Figure {figure}'.format(figure=figure))
    
    canvas.delete('all')
    a = canvas.create_rectangle(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill='red')
    b = canvas.create_rectangle(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill='blue')

def savewebdrivertorso(e=None):
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    
    ImageGrab.grab(bbox=(x, y, x1, y1)).save("figures/figure{figure}.png".format(figure=figure))

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

genbtn = tk.Button(root, command=webdrivertorso, text="Generate")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)

file_menu.add_command(label="Save", command=savewebdrivertorso)
file_menu.add_command(label="Save As...", command=saveaswebdrivertorso)

menubar.add_cascade(label="File", menu=file_menu)

canvas.grid(row=0, column=0)
genbtn.grid(row=1, column=0)

root.bind("<Control-n>", webdrivertorso)
root.bind("<Control-s>", savewebdrivertorso)
root.bind("<Control-S>", saveaswebdrivertorso)

webdrivertorso()

root.mainloop()
