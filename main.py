from tkinter import *
from tkinter import ttk
import pyqrcode
from ttkthemes import ThemedTk

def sub(event=None):
    global image
    if len(url.get()) > 0:
        qr = pyqrcode.create(url.get())
        qr.png('qr.png', scale=7)
        image = PhotoImage(file='qr.png')
        qr_lbl['image'] = image

root = ThemedTk(theme='yaru')
root.title('QR Code')
root.config(bg='white')

url = StringVar()

lbl1 = Label(root, bg='white', text='Type the url below', font=('Helvetica', 10, 'bold'))
lbl1.pack(pady=5, padx=20)

entry1 = ttk.Entry(root, textvar=url, width=30, justify=CENTER, font=('Helvetica', 10))
entry1.pack(pady=5, padx=20)

qr_lbl = Label(root, bg='white')
qr_lbl.pack(pady=10)

btn = ttk.Button(root, text='Submit', command=sub)
btn.pack(side=BOTTOM, pady=10)

root.bind('<Return>', sub)
root.mainloop()
