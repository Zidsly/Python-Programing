from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Car Class")
root.state('zoomed')

# Button Command
def classMPV():
    root.destroy()
    import MPV

def classSUV():
    root.destroy()
    import SUV

def classSprt():
    root.destroy()
    import Sport



bg = PhotoImage(file =r"C:\Users\user\Downloads\BGCARRENTAL1.png")

# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
canvas1.create_text(767, 50, text="ZEN CAR RENTAL", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

canvas1.create_text(767, 180, text="Pilih Kelas Mobil: ", fill='red3', anchor='center', font=("Helvetica", "25"))

# define font
myFont = font.Font(size=18)

# Create Buttons
button1 = Button(root, text="Kelas MPV", fg='violet red', bg='azure2', command=classMPV)
button2 = Button(root, text="Kelas SUV", fg='violet red', bg='azure2', command=classSUV)
button3 = Button(root, text="Kelas Sport", fg='violet red', bg='azure2', command=classSprt)

# apply font to the button label
button1['font'] = myFont
button2['font'] = myFont
button3['font'] = myFont

# Display Buttons
button1_canvas = canvas1.create_window(400, 150, height= 40, width=130,
                                       anchor="nw",
                                       window=button1)
button1.place(relx=0.5, rely=0.30, anchor='center')

button2_canvas = canvas1.create_window(400, 200, height= 40, width=130,
                                       anchor="nw",
                                       window=button2)
button2.place(relx=0.5, rely=0.40, anchor='center')


button3_canvas = canvas1.create_window(400, 250, height= 40, width=130,anchor="nw",
                                       window=button3)
button3.place(relx=0.5, rely=0.50, anchor='center')


# Execute tkinter
root.mainloop()