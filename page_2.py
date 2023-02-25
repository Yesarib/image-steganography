from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import page_1 as pg1

master = Tk()
canvas = Canvas(master, height=650, width=650)
canvas.pack()


def prevPage():
    master.destroy()

Button(
    master,
    text="Resim Gizlemek İçin Tıklayınız",
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

frame_mid1 = Frame(bg='')
frame_mid1.place(x=20, y=70, height=30, width=600)

dosya_yolu_text = Label(text='Resmi seçiniz', font='Verdana 12 bold')
dosya_yolu_text.place(x=20, y=40)
path = Label(frame_mid1,font='bold',bg='white')
path.pack(side=LEFT)

open_button = Button(text="Dosya Aç", command=lambda: [coz()], )
open_button.place(x=520, y=110, height=30, width=100)

panel = Label(master)
panel.place(x=20,y=140)


def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[("Images Files", '*.*')])
    if file:
        filepath = os.path.abspath(file.name)
        path.configure(text=filepath)
        open_image(file.name)
        return file.name


def get_path():
    file_path = (decode_text["text"])
    fp = str(file_path)

    print(fp)


def open_image(file):
    img = Image.open(file)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel.image = img
    panel.configure(image=img)

def coz():
    fp = open_file()
    text = decode(fp)
    decode_text.configure(text=text)
    print(text)



def decode(img):
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''
        # print(pixels)
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data


decode_text_msg = Label(text='Resmin içindeki gizlenmiş mesaj ',font='Verdana 12 bold')
decode_text_msg.place(x=20,y=370)

decode_frame = Frame(bg='white')
decode_frame.place(x=20,y=400,height=150,width=600)

decode_text = Label(decode_frame,bg='white',wraplength=550)
decode_text.pack(side=LEFT)

master.mainloop()
