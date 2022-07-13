from tkinter import *

window = Tk()
window.title("Mile To Km Convertor")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

# equal text
equal_text = Label(text="is equal to", padx=5)
equal_text.grid(column=0, row=1)


def button_got_clicked():
    mile = int_mile.get()
    km = round(mile*1.609344)
    km_label.config(text=km)


# entry of mile
int_mile = IntVar()
no_of_miles = Entry(width=8, textvariable=int_mile)
# no_of_miles.insert(END, string=0)
no_of_miles.grid(column=1, row=0)

# mile text
mile_text = Label(text="Mile")
mile_text.grid(column=2, row=0)

# km label
km_label = Label(text=0)
km_label.grid(column=1, row=1)

# km text
km_text = Label(text="km")
km_text.grid(column=2, row=1)

# calculate button
cal_button = Button(text="Calculate", command=button_got_clicked)
cal_button.grid(column=1, row=2)


window.mainloop()
