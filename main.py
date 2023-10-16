from tkinter import *  # Importing the tkinter module for GUI
FONT = ("Arial", 12)  # Setting the font style and size

window = Tk()  # Creating a tkinter window
window.title("Mile to Km converter")  # Setting the title of the window
window.config(padx=10, pady=10)  # Configuring the padding of the window

user_input = Entry(width=10)  # Creating an entry widget for user input
user_input.grid(column=1, row=0)  # Placing the widget in the window

miles = Label(text="Miles", font=FONT)  # Creating a label widget
miles.grid(column=2, row=0)  # Placing the widget in the window

is_equal_to = Label(text="is equal to", font=FONT)  # Creating another label widget
is_equal_to.grid(column=0, row=1)  # Placing the widget in the window

result_value = Label(text="0", font=FONT)  # Creating a label to display the result
result_value.grid(column=1, row=1)  # Placing the widget in the window

km = Label(text="Km", font=FONT)  # Creating a label widget for "Km"
km.grid(column=2, row=1)  # Placing the widget in the window


def on_click():
    miles_from_user = user_input.get()  # Getting input from user
    formula = float(miles_from_user) * 1.609  # Converting miles to km
    result_value.config(text=formula)  # Displaying the result on label


button = Button(text="Calculate", font=FONT, command=on_click)
# Creating a button that will call on_click function when pressed

button.grid(column=1, row=3)  # Placing the button widget in the window

window.mainloop()  # Starting the tkinter event loop
