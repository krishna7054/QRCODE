import qrcode
from tkinter import *
import PIL


def gg_code():
    a1 = qrcode.QRCode(box_size=35, border=5)

    a1.add_data("https://krishna7054.github.io/krishnacv/")

    a1.make(fit=True)

    g_qr = a1.make_image(fill_color="black", back_color="white")

    g_qr.save("live_2.png")

    a3=Label(w, text= "QR CODE GENERATED", background="lightpink", fg="black", font=("Arial", 35, "bold"))
    a3.pack()


w = Tk()
w.config(bg="yellow")
w.geometry("500x500")
w.title("OWN QRCODE")

a2 = Label(w, text="QR CODE GENERATOR", background="black", fg="red",  font=("Arial", 35, "bold"))

a2.pack()

b1 = Button(w, text="CREATE", background="pink", fg="green", font=("Arial", 35, "bold"), command=gg_code)

b1.pack()

w.mainloop()