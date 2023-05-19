from tkinter import *

def miles_to_km():
    miles = float(input_entry.get())
    km = miles * 1.609
    answer_label["text"] = f"{km}"

window = Tk()
window.title("Miles to Kilometers Converter")

my_label = Label(window, text="Miles to Kilometers")
my_label.pack(padx=50, pady=50)

input_entry = Entry(window, width=10)
input_entry.pack()

button = Button(window, text="Calculate", command=miles_to_km)
button.pack()

answer_label = Label(window, text="0")
answer_label.pack()

window.mainloop()
