from tkinter import *
import tkinter.font as font

root = Tk()
root.title("tkinter bg test")
root.state('zoomed')

# Button Command
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

canvas1.create_text(767, 300, text="Syarat dan Ketentuan \n 1.  Sewa Mobil belum termasuk Driver \n "
                                  "2.  Booking min 2 (dua) hari sebelum keberangkatan \n "
                                  "3.  Biaya belum termasuk : tol, bensin,dan Parkir \n"
                                  "4.  Penyewa dilarang menggadaikan kendaraan \n "
                                  "5.  Penyewa dilarang menyewakan kembali kepada orang lain \n "
                                  "6.  Penyewa dilarang menjual kendaraan \n "
                                  "7.  Penyewa dilarang memindah tangankan sewa \n "
                                  "8.  Penyewa dilarang menggunakan mobil untuk tindak kejahatan \n "
                                  "9.  Penyewa dilarang menaikan harga sewa dari penawaran kami (Mark Up) \n "
                                  "10. Penyewa dilarang mendaraan hanya dapat dikemudikan oleh orang yang memiliki SIM"
, fill='white', anchor='center', font=("Helvetica", "20", "bold italic"))

# Button
Button(root, text=("Kembali"), command=back, height=3, width=12).place(x=680, y=650)

root.mainloop()