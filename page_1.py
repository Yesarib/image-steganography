from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog


master = Tk()
canvas = Canvas(master,height=650, width=650)
canvas.pack()

def nextPage():
    master.destroy()
    import page_2
Button(
    master,
    text="Resmi Çözmek İçin Tıklayınız",
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)


frame_mid1 = Frame(master, bg='')
frame_mid1.place(x=20,y=70,height=30,width=300)

dosya_yolu_text = Label(master, text='Dosya Yolu', font='Verdana 12 bold')
dosya_yolu_text.place(x=20, y=40)

open_button = Button(master, text="Dosya Aç", command=lambda: [open_file(),get_path()],)
open_button.place(x=220,y=110,height=30,width=100)

path_label = Label(frame_mid1,bg='white',font='bold')
path_label.pack(side=LEFT)

image_frame = Label(master)
image_frame.place(x=20,y=600)
panel = Label(master,)
panel.place(x=350,y=50)


def open_file():
    file = filedialog.askopenfile(title='open', filetypes=[("Images Files", '*.*')])
    if file:
        path_label.configure(text=file.name)
        open_image(file.name)

def open_image(file):
    img = Image.open(file)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    panel.image = img
    panel.configure(image=img)

def save_file():
    file = filedialog.asksaveasfilename(filetypes=[("Images Files", '*.png')])
    if file:
        return file

def get_path():
    file_path = (path_label["text"])
    fp = str(file_path)
    return fp


def display_text():
    txt = text_input.get(1.0, "end-1c")
    return txt


def gizle():
    encode(get_path(), display_text())


file_path_label = Label(frame_mid1, text=get_path(), font='Verdana 12', bg='white')
file_path_label.pack(side=LEFT)

# input alma kısmı tam değil
mesaj_text = Label(master, text='Gizlemek istediğiniz mesaj', font='Verdana 12 bold', fg='blue' )
mesaj_text.place(x=20, y=300)

text_input = Text(master)
text_input.place(x=20,y=330,width=600,height=150)

send_button = Button(master, text="Gizle", command=lambda: [gizle(),info()])
send_button.place(x=520, y=510, height=30, width=100 )


save_file_label = Label(master, text='Yeni Resmi Kaydetmek İçin Tıklayınız', font='Verdana 12 bold')
save_file_label.place(x=20, y=510)

save_path_label = Label(bg='white',font='bold')
save_path_label.pack(side=LEFT)

        # BİLGİLENDİRME
frame_bottom = Frame(master, bg='#FFFFFF')
frame_bottom.place(x=20,y=580)
success = False
success_text = Label(frame_bottom, text="",font=('Helvetica 13'))
success_text.pack()


def info():
    msg = 'Mesajınız başarıyla resme gizlendi ve yeni resim oluşturuldu.'
    success_text.configure(text=msg)

def encode(img, data):
    image = Image.open(img, 'r')

    newimg = image.copy()
    encode_enc(newimg, data)
    new_image_name = "new.png"
    newimg.save(save_file(), str(new_image_name.split(".")[1].upper()))


def encode_enc(newimg, data):
    width_image = newimg.size[0]
    print(width_image)
    (x, y) = (0, 0)
    # print(list(newimg.getdata()))
    for pixel in modPix(newimg.getdata(), data):

        #
        newimg.putpixel((x, y), pixel)
        if x == width_image - 1:
            x = 0
            y += 1
        else:
            x += 1

def genData(data):
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    print(datalist)
    # print(lendata)

    for i in range(lendata):

        pix = [value for value in imdata.__next__()[:3] +
                imdata.__next__()[:3] +
                imdata.__next__()[:3]]
        # print("modPix içindeki :",pix)

        for j in range(0, 8):
            if datalist[i][j] == '0' and pix[j] % 2 != 0:
                pix[j] -= 1

            elif datalist[i][j] == '1' and pix[j] % 2 == 0:
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
            # pix[j] -= 1
        # print(pix)

        # -----
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


master.mainloop()


