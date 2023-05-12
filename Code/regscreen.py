from tkinter import *
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("tkinter bg test")
root.state('zoomed')

# Button Commands
def regop():
    op = open("database.txt", "r")
    Username = e1.get()
    password = e7.get()
    passwordclr = e8.get()
    x = []
    y = []
    for i in op:
        a,b = i.split(", ")
        b = b.strip()
        x.append(a)
        y.append(b)
        data = dict(zip(x, y))

    if(password != passwordclr):
        messagebox.showinfo("", "Password anda tidak sama, mohon coba lagi")
    else:
        if(len(password) <= 6):
            messagebox.showinfo("", "Password anda terlalu pendek, mohon coba lagi")
        elif(Username in op):
            messagebox.showinfo("", "Username ini sudah digunakan, mohon coba lagi")
        else:
            op = open("database.txt", "a")
            op.write(Username+", "+password+"\n")
            messagebox.showinfo("", "Register anda sukses!")
            root.destroy()
            import carclass

def back():
    root.destroy()
    import CarRentalSystem

bg = PhotoImage(file =r"r"C:\Users\user\Downloads\BGCARRENTAL1.png")

# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
canvas1.create_text(767, 80, text="ZEN CAR RENTAL", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

# Label Placement
text1=Label(root, text='Username', font=("Arial", 18))
text1.place(x=350, y=200)

text2=Label(root, text='Nama Panjang', font=("Arial", 18))
text2.place(x=350, y=250)

text3=Label(root, text='Email', font=("Arial", 18))
text3.place(x=350, y=300)

text4=Label(root, text='Alamat', font=("Arial", 18))
text4.place(x=350, y=350)

text5=Label(root, text='No. KTP', font=("Arial", 18))
text5.place(x=350, y=400)

text6=Label(root, text='No. HP', font=("Arial", 18))
text6.place(x=350, y=450)

text7=Label(root, text='Password', font=("Arial", 18))
text7.place(x=350, y=500)

text8=Label(root, text='Password', font=("Arial", 18))
text8.place(x=350, y=550)

# Entry Placement
e1 = Entry(root, width=54, font=("Arial", 18))
e1.place(x=470, y=200)

e2 = Entry(root, width=50, font=("Arial", 18))
e2.place(x=520, y=250)

e3 = Entry(root, width=54, font=("Arial", 18))
e3.place(x=470, y=300)

e4 = Entry(root, width=54, font=("Arial", 18))
e4.place(x=470, y=350)

e5 = Entry(root, width=54, font=("Arial", 18))
e5.place(x=470, y=400)

e6 = Entry(root, width=54, font=("Arial", 18))
e6.place(x=470, y=450)

e7 = Entry(root, width=54, font=("Arial", 18))
e7.place(x=470, y=500)

e8 = Entry(root, width=54, font=("Arial", 18))
e8.place(x=470, y=550)
e8.insert(0, 'Masukkan password lagi')

# Button
Button(root, text=("Register"), command=regop, height=2, width=10).place(x=680, y=750)
Button(root, text=("Kembali"), command=back, height=2, width=10).place(x=780, y=750)

root.mainloop()