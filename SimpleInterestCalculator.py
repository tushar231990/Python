from tkinter import *

def calculate_SI():
    principle = int(principle_field.get())
    interest = float(Rate_field.get())
    time = int(time_field.get())

    simple_interest = (principle*interest*time)/100
    amount = principle+simple_interest

    Interest_Field.insert(10,simple_interest)
    Amount_Field.insert(10,amount)


def clear_app():
    principle_field.delete(0,END)
    Rate_field.delete(0,END)
    time_field.delete(0,END)
    Interest_Field.delete(0,END)
    Amount_Field.delete(0,END)
    principle_field.focus_set()

root = Tk()

root.configure(background="grey")
root.geometry("1000x500")
root.title("Simple interest calculator")

font="Arial"

label1 = Label(root,text="Enter Principle amount",font=font,bg="blue",fg="white")
label2 = Label(root,text="Enter time in years",font=font,bg="blue",fg="white")
label3 = Label(root,text="Enter interest percentace",font=font,bg="blue",fg="white")
label4 = Label(root,text="Calculated Simple interest",font=font,bg="blue",fg="white")
label5 = Label(root,text="Calculated total amount",font=font,bg="blue",fg="white")

label1.grid(row=1,column=0,padx=10,pady=10)
label2.grid(row=2,column=0,padx=10,pady=10)
label3.grid(row=3,column=0,padx=10,pady=10)
label4.grid(row=4,column=0,padx=10,pady=10)
label5.grid(row=5,column=0,padx=10,pady=10)

principle_field = Entry(root)
time_field = Entry(root)
Rate_field = Entry(root)
Interest_Field = Entry(root)
Amount_Field = Entry(root)

principle_field.grid(row=1,column=1,padx=10,pady=10)
time_field.grid(row=2,column=1,padx=10,pady=10)
Rate_field.grid(row=3,column=1,padx=10,pady=10)
Interest_Field.grid(row=4,column=1,padx=10,pady=10)
Amount_Field.grid(row=5,column=1,padx=10,pady=10)

calculate_button = Button(root,text="Calculate",command=calculate_SI)
calculate_button.grid(row=6,column=2,padx=10,pady=10)

delete_button = Button(root,text="Clear",command=clear_app)
delete_button.grid(row=6,column=3,padx=10,pady=10)

root.mainloop()
