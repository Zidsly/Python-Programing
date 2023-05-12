from tkinter import *
import tkinter.font as font

root = Tk()
root.title("tkinter bg test")
root.state('zoomed')

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

canvas1.create_text(767, 400, text="TERIMA KASIH!", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))



root.destroy()

root.mainloop()