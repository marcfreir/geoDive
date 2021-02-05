from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plot

root = Tk()
root.title("GeoDive - v. 0.01")
# root.iconbitmap("../img/geodive.ico")
root.geometry("400x200")

def graph():
    r_numbers = np.random.normal(2000, 3500, 4000)
    plot.hist(r_numbers, 50)
    plot.show()

btn_show_graph = Button(root, text="Plot", command=graph)
btn_show_graph.pack()

root.mainloop()