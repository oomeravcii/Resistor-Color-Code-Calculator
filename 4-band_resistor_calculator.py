import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

window = tk.Tk()
window.geometry("500x500+400+200")
window.title("Direnç Değeri Hesaplama")
window.config(bg="red")


# 4 Bantlı Direnç:

label4 = tk.Label(window,text="4 Bantlı Dirençler İçin Renk Kodu Okuma:",bg="black",fg="white",font="verdana 10 bold")
label4.place(x=10,y=50)

liste1 = ["Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"]
kutu1 = Combobox(window,values=liste1)
kutu1.place(x=10,y=90,width=80)

liste2 = ["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"]
kutu2 = Combobox(window,values=liste2)
kutu2.place(x=100,y=90,width=80)

liste3 = ["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Altın","Gümüş"]
kutu3 = Combobox(window,values=liste3)
kutu3.place(x=190,y=90,width=80)

liste4 = ["Kahverengi","Kırmızı","Altın","Gümüş"]
kutu4 = Combobox(window,values=liste4)
kutu4.place(x=280,y=90,width=80)


def hesapla():
    if len(kutu1.get()) == 0 or len(kutu2.get()) == 0 or len(kutu3.get()) == 0 or len(kutu4.get()) == 0:
        messagebox.showerror(title="Hata!",message="Tüm kutuları doldurunuz.")
    else:
        sozluk1 = {"Siyah":0,"Kahverengi":1,"Kırmızı":2,"Turuncu":3,"Sarı":4,"Yeşil":5,"Mavi":6,"Mor":7,"Gri":8,"Beyaz":9}
        sozluk2 = {"Siyah":1,"Kahverengi":10,"Kırmızı":100,"Turuncu":1000,"Sarı":10000,"Yeşil":100000,"Mavi":1000000,"Altın":0.1,"Gümüş":0.01}
        sozluk3 = {"Kahverengi":1,"Kırmızı":2,"Altın":5,"Gümüş":10}
        deger1 = kutu1.get()
        deger2 = kutu2.get()
        deger3 = kutu3.get()
        deger4 = kutu4.get()
        
        ohm = str(sozluk1[deger1])+str(sozluk1[deger2])+"x"+str(sozluk2[deger3])+"="+str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk2[deger3])[1:]+" ohm"
        tolerans = "%"+str(sozluk3[deger4])+" tolerans"
        label_ohm = tk.Label(window,text=ohm)
        label_ohm.place(x=10,y=120)
        label_tolerans = tk.Label(window,text=tolerans)
        label_tolerans.place(x=10,y=150)

buton1 = tk.Button(window,text="Hesapla",command=hesapla)
buton1.place(x=380,y=87)




window.mainloop()