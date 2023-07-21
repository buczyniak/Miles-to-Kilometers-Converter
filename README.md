# Miles-to-Kilometers-Converter

![converter](https://github.com/buczyniak/Miles-to-Kilometers-Converter/assets/78871310/6da3fc14-404b-4710-81bf-ff02af07cef8)

## Introduction - What the Miles to Kilometer Converter does
The Miles to Kilometer Converter is an application that helps users convert distances from miles to kilometers. 
It provides a quick and easy way to perform this conversion, making it convenient for anyone who needs to work 
with distance measurements in both miles and kilometers.

The Converter was created while taking a [Udemy course](https://www.udemy.com/course/100-days-of-code/).

## Explanation of the Code
The Python code is a basic graphical application using the Tkinter library for the user interface. 
Let's walk through the main components of the code.

### Conversion Function:
```
def convert():
    miles_to_convert = float(textbox1.get())
    kilometers_converted = miles_to_convert * 1.60934
    label2.config(text=f"is {kilometers_converted} km")
```
The convert() function is responsible for converting the distance entered by the user from miles to 
kilometers. When the "Convert miles to km" button is clicked, this function is executed. It takes the 
input value from the textbox, converts it to a float, performs the conversion (multiplying the miles by 
1.60934), and updates the result in the label (label2) below the textbox.

### User Interface Setup:
```
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
```
The code creates a graphical user interface (GUI) using Tkinter. The GUI consists of:

* A window titled "Miles to Kilometer Converter."
* An input textbox (textbox1) where the user can enter the distance in miles.
* A label (label1) displaying "miles" next to the textbox to indicate the unit of input.
* Another label (label2) to display the converted distance in kilometers after the conversion.
* A button (button) labeled "Convert miles to km" to trigger the conversion when clicked.

### Conversion Process:
1. The user enters the distance in miles in the textbox (textbox1).
1. When the user clicks the "Convert miles to km" button, the convert() function is called.
1. The function reads the input value from the textbox, converts it to a floating-point number, and stores 
it in the variable miles_to_convert.
1. The function then multiplies miles_to_convert by the conversion factor 1.60934 to get the equivalent 
distance in kilometers, which is stored in the variable kilometers_converted.
1. The result is displayed in the label (label2) below the textbox, showing the converted distance in kilometers.

### Summary
Overall, the Miles to Kilometer Converter GUI provides a straightforward way for users to perform distance 
conversions from miles to kilometers. It enables users to quickly and accurately convert distances without the 
need for manual calculations.
