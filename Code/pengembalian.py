from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Main menu")
root.state('zoomed')

bg = PhotoImage(file =r"C:\Users\user\Downloads\BGCARRENTAL1.png")

# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

def back():
    root.destroy()
    import CarRentalSystem
def exit():
    root.destroy()
    import exitscreen

# Add Text
canvas1.create_text(767, 80, text="ZEN CAR RENTAL", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

# define font
myFont = font.Font(size=18)

# Add Text
canvas1.create_text(767, 400, text="TERIMA KASIH TELAH MENGEMBALIKAN MOBIL ANDA", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

#Add Button
Button(root, text=("HomeScreen"), command=back, height=2, width=10).place(x=780, y=500)
Button(root, text=("Exit"), command=exitscreen, height=2, width=10).place(x=880, y=500)

root.mainloop()