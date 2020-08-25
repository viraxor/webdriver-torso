from tkinter import *
from random import randint as rnd
from PIL import ImageGrab

root = Tk()
figure = 0

root.title('Webdriver Torso')

canvas = Canvas(root, width=820, height=550)

def webdrivertorso():
    global figure
    canvas.delete('all')
    figure += 1
    root.title('Webdriver Torso - Figure ' + str(figure))
    a = canvas.create_oval(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill='red')
    b = canvas.create_oval(rnd(0, 820), rnd(0, 550), rnd(0,820), rnd(0, 550), width=0, fill='blue')

def savewebdrivertorso():
    x=root.winfo_rootx()+canvas.winfo_x()
    y=root.winfo_rooty()+canvas.winfo_y()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save("figures/figure" + str(figure) + ".png")

btn = Button(root, text="Generate", command=webdrivertorso)
btn2 = Button(root, text="Save", command=savewebdrivertorso)

canvas.grid(row=0, column=0)
btn.grid(row=1, column=1)
btn2.grid(row=1, column=0)

root.mainloop()


