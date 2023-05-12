from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Main menu")
root.state('zoomed')

# Button Commands
def login():
    root.destroy()
    import loginscreen

def register():
    root.destroy()
    import regscreen

def rules():
    root.destroy()
    import rulescreen

def exit():
    root.destroy()
    import exitscreen

def Pengembalian():
    root.destroy()
    import loginscreen2

bg = PhotoImage(file =r"C:\Users\user\Downloads\BGCARRENTAL1.png")

# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
canvas1.create_text(767, 80, text="ZEN CAR RENTAL", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

# define font
myFont = font.Font(size=18)

# Create Buttons
button1 = Button(root, text="Login", fg='red3', bg='azure2', command=login)
button2 = Button(root, text="Register", fg='red3', bg='azure2', command=register)
button3 = Button(root, text="Syarat dan ketentuan", fg='red3', bg='azure2', command=rules)
button4 = Button(root, text="Exit", fg='red3', bg='azure2', command=exit)
button5 = Button(root, text="Pengembalian", fg='red3', bg='azure2', command=Pengembalian)

# apply font to the button label
button1['font'] = myFont
button2['font'] = myFont
button3['font'] = myFont
button4['font'] = myFont
button5['font'] = myFont

# Display Buttons
button1_canvas = canvas1.create_window(400, 150, height= 40, width=100,
                                       anchor="nw",
                                       window=button1)
button1.place(relx=0.5, rely=0.30, anchor='center')

button2_canvas = canvas1.create_window(400, 200, height= 40, width=130,
                                       anchor="nw",
                                       window=button2)
button2.place(relx=0.5, rely=0.40, anchor='center')


button3_canvas = canvas1.create_window(400, 250, height= 40, width=250,anchor="nw",
                                       window=button3)
button3.place(relx=0.5, rely=0.50, anchor='center')

button5_canvas = canvas1.create_window(400, 300, height= 40, width=85, anchor="nw",
                                       window=button4)
button5.place(relx=0.5, rely=0.60, anchor='center')

button4_canvas = canvas1.create_window(400, 350, height= 40, width=85, anchor="nw",
                                       window=button4)
button4.place(relx=0.5, rely=0.70, anchor='center')


# Execute tkinter
root.mainloop()