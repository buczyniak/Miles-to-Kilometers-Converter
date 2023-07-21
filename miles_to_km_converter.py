from tkinter import *


def convert():
    miles_to_convert = float(textbox1.get())
    kilometers_converted = miles_to_convert * 1.60934
    label2.config(text=f"is {kilometers_converted} km")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=230, height=140)

textbox1 = Entry()
textbox1.grid(column=1, row=1, pady=20, padx=20)

label1 = Label(text="miles")
label1.grid(column=2, row=1)

label2 = Label()
label2.grid(column=1, row=2)

button = Button(text="Convert miles to km", command=convert)
button.grid(column=1, row=3)

window.mainloop()
