from tkinter import *
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("LOGIN")
root.state('zoomed')

# Button Commands
def loginop():
    global Username
    op = open("database.txt", "r")
    Username = e1.get()
    password = e2.get()

    if(not len(Username or password) < 1):
        x = []
        y = []
        for i in op:
            a, b = i.split(", ")
            b = b.strip()
            x.append(a)
            y.append(b)
        data = dict(zip(x, y))

        try:
            if(data[Username]):
                try:
                    if(password == data[Username]):
                        messagebox.showinfo("", "Login Sukses!")
                        root.destroy()
                        import pengembalian
                    else:
                        messagebox.showinfo("", "Username atau Password anda salah!")
                except:
                    messagebox.showinfo("", "Username atau Password anda salah!")
            else:
                messagebox.showinfo("", "Username ini tidak ada")
        except:
            messagebox.showinfo("", "Username ini tidak ada")




def back():
    root.destroy()
    import CarRentalSystem

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
myFont = font.Font(size=30)


# Label Placement
text1=Label(root, text='Username', font=("Arial", 18))
text1.place(x=350, y=350)

text2=Label(root, text='Password', font=("Arial", 18))
text2.place(x=350, y=400)

# Entry Placement
e1 = Entry(root, width=50, font=("Arial", 18))
e1.place(x=470, y=350)

e2 = Entry(root, width=50, font=("Arial", 18))
e2.place(x=470, y=400)
e2.config(show="*")

# Button
Button(root, text=("login"), command=loginop, height=2, width=10).place(x=680, y=500)
Button(root, text=("Kembali"), command=back, height=2, width=10).place(x=780, y=500)

root.mainloop()