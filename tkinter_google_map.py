from tkinter import *
import tkintermapview
from tkinter import ttk

root = Tk()
root.title("Google map with address search")
root.geometry("900x680")

def lookup():
    map_widget.set_address(my_entry.get())
    my_slider.config(value=9)

def slider(e):
    map_widget.set_zoom(my_slider.get())

my_label = LabelFrame(root)
my_label.pack(pady=20)
map_widget = tkintermapview.TkinterMapView(my_label, width=850, height=480,corner_radius=0)
#map_widget.set_position(52.3555, 1.1743)
map_widget.set_address("England")
map_widget.pack()
my_frame = LabelFrame(root)
my_frame.pack(pady=10)
my_entry = Entry(my_frame, font=('Helvetica', 28))
my_entry.grid(row=0, column=0, pady=10, padx=10)
my_button = Button(my_frame, text="LookUp", font=('Helvetica', 18), command=lookup)
my_button.grid(row=0, column=1, padx=10)
my_slider = ttk.Scale(my_frame, from_=4, to=20, orient=HORIZONTAL, command=slider, value=20, length=220)
my_slider.grid(row=0, column=2, padx=10)
root.mainloop()