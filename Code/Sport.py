from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import tkinter.font as font

root = Tk()
root.title("MPV")
root.state('zoomed')

bg = PhotoImage(file =r"C:\Users\user\Downloads\BGCARRENTAL1.png")

# Button Commands
def MPVop():
    global IDCar
    IDCar = e1.get()
    if(IDCar == '7'):
        text1.destroy()
        text2.destroy()
        text3.destroy()
        text4.destroy()
        text5.destroy()
        text6.destroy()
        text7.destroy()
        text8.destroy()
        text9.destroy()
        text10.destroy()
        text11.destroy()
        text12.destroy()
        text13.destroy()
        text14.destroy()
        text15.destroy()
        text16.destroy()
        text17.destroy()
        e1.destroy()
        button1.destroy()
        textord = Label(root, text='Berapa lama mobil akan dirental(dalam jam)', font=("Arial", 18), width=35)
        textord.place(x=150, y=125)
        e2 = Entry(root, width=55, font=("Arial", 19))
        e2.place(x=650, y=125)
        def purchase1():
            global jam
            global hargattl
            num = e2.get()
            jam = int(num)
            price = 3200000
            hargattl = jam / 24 * price
            textttl = Label(root, text='Total harga anda adalah %s' % hargattl, font=("Arial", 18), width=91)
            textttl.place(x=150, y=200)
            button2.destroy()
            struk()
            def exit():
                root.destroy()
                import exitscreen
            def done():
                root.destroy()
                import CarRentalSystem
            button3 = Button(root, text=("Exit"), command=exit, height=2, width=10)
            button3.place(x=750, y=400)
            button4 = Button(root, text=("Homescreen"), command=done, height=2, width=10)
            button4.place(x=850, y=400)
        button2 = Button(root, text=("Continue"), command=purchase1, height=2, width=10)
        button2.place(x=750, y=400)
    elif(IDCar == '8'):
        text1.destroy()
        text2.destroy()
        text3.destroy()
        text4.destroy()
        text5.destroy()
        text6.destroy()
        text7.destroy()
        text8.destroy()
        text9.destroy()
        text10.destroy()
        text11.destroy()
        text12.destroy()
        text13.destroy()
        text14.destroy()
        text15.destroy()
        text16.destroy()
        text17.destroy()
        e1.destroy()
        button1.destroy()
        textord = Label(root, text='Berapa lama mobil akan dirental(dalam jam)', font=("Arial", 18), width=35)
        textord.place(x=150, y=125)
        e2 = Entry(root, width=55, font=("Arial", 19))
        e2.place(x=650, y=125)
        def purchase1():
            global jam
            global hargattl
            num = e2.get()
            jam = int(num)
            price = 1700000
            hargattl = jam / 24 * price
            textttl = Label(root, text='Total harga anda adalah %s' % hargattl, font=("Arial", 18), width=91)
            textttl.place(x=150, y=200)
            button2.destroy()
            struk()
            def exit():
                root.destroy()
                import exitscreen
            def done():
                root.destroy()
                import CarRentalSystem
            button3 = Button(root, text=("Exit"), command=exit, height=2, width=10)
            button3.place(x=750, y=400)
            button4 = Button(root, text=("Homescreen"), command=done, height=2, width=10)
            button4.place(x=850, y=400)
        button2 = Button(root, text=("Continue"), command=purchase1, height=2, width=10)
        button2.place(x=750, y=400)
    elif(IDCar == '9'):
        text1.destroy()
        text2.destroy()
        text3.destroy()
        text4.destroy()
        text5.destroy()
        text6.destroy()
        text7.destroy()
        text8.destroy()
        text9.destroy()
        text10.destroy()
        text11.destroy()
        text12.destroy()
        text13.destroy()
        text14.destroy()
        text15.destroy()
        text16.destroy()
        text17.destroy()
        e1.destroy()
        button1.destroy()
        textord = Label(root, text='Berapa lama mobil akan dirental(dalam jam)', font=("Arial", 18), width=35)
        textord.place(x=150, y=125)
        e2 = Entry(root, width=55, font=("Arial", 19))
        e2.place(x=650, y=125)
        def purchase1():
            global jam
            global hargattl
            num = e2.get()
            jam = int(num)
            price = 5500000
            hargattl = jam / 24 * price
            textttl = Label(root, text='Total harga anda adalah %s' % hargattl, font=("Arial", 18), width=91)
            textttl.place(x=150, y=200)
            button2.destroy()
            struk()
            def exit():
                root.destroy()
                import exitscreen
            def done():
                root.destroy()
                import CarRentalSystem
            button3 = Button(root, text=("Exit"), command=exit, height=2, width=10)
            button3.place(x=750, y=400)
            button4 = Button(root, text=("Homescreen"), command=done, height=2, width=10)
            button4.place(x=850, y=400)
        button2 = Button(root, text=("Continue"), command=purchase1, height=2, width=10)
        button2.place(x=750, y=400)
    else:
        messagebox.showinfo("", "Maaf itu bukan pilihan")


# Create Canvas
canvas1 = Canvas(root, width=800,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

# Add Text
canvas1.create_text(767, 80, text="ZEN CAR RENTAL", fill='red3', anchor='center', font=("Helvetica", "30", "bold italic"))

# Add Label
text1 = Label(root, text='ID Mobil', font=("Arial", 18), width=18)
text1.place(x=280,y=125)
text2 = Label(root, text='Nama Mobil', font=("Arial", 18), width=18)
text2.place(x=540,y=125)
text3 = Label(root, text='Plat Nomor', font=("Arial", 18), width=18)
text3.place(x=800,y=125)
text4 = Label(root, text='Harga Rental', font=("Arial", 18), width=18)
text4.place(x=1060,y=125)
text5 = Label(root, text='7', font=("Arial", 18), width=18)
text5.place(x=280,y=160)
text6 = Label(root, text='8', font=("Arial", 18), width=18)
text6.place(x=280,y=195)
text7 = Label(root, text='9', font=("Arial", 18), width=18)
text7.place(x=280,y=230)
text8 = Label(root, text='Nissan, R32 Skyline GTR', font=("Arial", 18), width=18)
text8.place(x=540,y=160)
text9 = Label(root, text='Honda, Civic Type-R', font=("Arial", 18), width=18)
text9.place(x=540,y=195)
text10 = Label(root, text='Ferrari, F8 Tributo', font=("Arial", 18), width=18)
text10.place(x=540,y=230)
text11 = Label(root, text='B 32 GTR', font=("Arial", 18), width=18)
text11.place(x=800,y=160)
text12 = Label(root, text='F 64 YPR', font=("Arial", 18), width=18)
text12.place(x=800,y=195)
text13 = Label(root, text='B  8  FER', font=("Arial", 18), width=18)
text13.place(x=800,y=230)
text14 = Label(root, text='3.200.000 / 24 jam', font=("Arial", 18), width=18)
text14.place(x=1060,y=160)
text15 = Label(root, text='1.700.000 / 24 jam', font=("Arial", 18), width=18)
text15.place(x=1060,y=195)
text16 = Label(root, text='5.500.000 / 24 jam', font=("Arial", 18), width=18)
text16.place(x=1060,y=230)
text17 = Label(root, text='Masukkan ID Mobil ', font=("Arial", 18), width=18)
text17.place(x=280,y=265)

# Add Entry
e1 = Entry(root, width=55, font=("Arial", 19))
e1.place(x=540, y=265)

# Add Button
button1 = Button(root, text=("Continue"), command=MPVop, height=2, width=10)
button1.place(x=750, y=400)

# display curent time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Write to Text File
def struk():
    f = open("strukRental.txt", "w")
    f.write("------------------------------------- " + "\n" +
            "-----      Nota Pembayaran      -----" + "\n" +
            "------------------------------------- " + "\n" +
            "ID Mobil = " + IDCar + "\n" +
            "Total Jam = " + str(jam) + "\n" +
            "Total Harga = " + str(hargattl) +"\n" +
            "Jam = " + current_time + "\n" +
            "------------------------------------- ")
    f.close()

    f = open("strukRental.txt", "r")
    print(f.read())

root.mainloop()

