from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pyglet
import tkinter.font as tkFont
#Настройка окна
root = Tk()
root.title("Iot-monitoring")
root.geometry("650x250")
root.resizable(False,False)
root.configure(bg='#f5badf')
icon = PhotoImage(file = "assets/icon.png")
root.iconphoto(False, icon)
pyglet.options['win32_gdi_font'] = True
pyglet.font.add_file('assets/path/Akedoakushon-Regular.otf')
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family="Akedoakushon-Regular", size=25)
#Размещение Gif
frames1, frames2, frames3, frames4 = [], [], [], []
try:
    with Image.open("assets/cat.gif") as gif:
        for frame in ImageSequence.Iterator(gif):
            resized_frame = frame.convert('RGBA').resize((60, 60), Image.Resampling.LANCZOS)
            frames1.append(ImageTk.PhotoImage(resized_frame))
    with Image.open("assets/jumper.gif") as gif:
        for frame in ImageSequence.Iterator(gif):
            resized_frame = frame.convert('RGBA').resize((80, 80), Image.Resampling.LANCZOS)
            frames2.append(ImageTk.PhotoImage(resized_frame))
    with Image.open("assets/heart.gif") as gif:
        for frame in ImageSequence.Iterator(gif):
            resized_frame = frame.convert('RGBA').resize((80, 80), Image.Resampling.LANCZOS)
            frames3.append(ImageTk.PhotoImage(resized_frame))
    with Image.open("assets/knife.gif") as gif:
        for frame in ImageSequence.Iterator(gif):
            resized_frame = frame.convert('RGBA').resize((40, 40), Image.Resampling.LANCZOS)
            frames4.append(ImageTk.PhotoImage(resized_frame))
except FileNotFoundError:
    print("Файлы не найдены.")
def update_gif(ind, frames, gif_label):
    if frames:
        frame = frames[ind]
        ind += 1
        if ind == len(frames):
            ind = 0
        gif_label.configure(image=frame)
        root.after(250, update_gif, ind, frames, gif_label)
if frames1:
    gif_label1 = Label(root, bg='#f5badf')
    gif_label1.place(x=587, y=187)
    root.after(0, update_gif, 0, frames1, gif_label1)
if frames2:
    gif_label2 = Label(root, bg='#f5badf')
    gif_label2.place(x=5, y=169)
    root.after(0, update_gif, 0, frames2, gif_label2)
if frames3:
    gif_label2 = Label(root, bg='#f5badf')
    gif_label2.place(x=572, y=40)
    root.after(0, update_gif, 0, frames3, gif_label2)
if frames4:
    gif_label2 = Label(root, bg='#f5badf')
    gif_label2.place(x=5, y=10)
    root.after(0, update_gif, 0, frames4, gif_label2)

#Текст
label = Label(text="temperature", bg="#f5badf")
label1 = Label(text="humidity", bg="#f5badf")
label2 = Label(text="current time:", bg="#f5badf")
label3 = Label(text="%", bg="#f5badf")
label4 = Label(text="°C", bg="#f5badf")

val_temp = Label(root, text="--", bg="#c8cbcc")
val_hum = Label(root, text="--", bg="#c8cbcc")
val_time = Label(root, text="--:--", bg="#c8cbcc")

#Размещение полученных значений
label.grid(row=0, column=0, sticky="w", padx=(60, 5), pady=15)  #temperature
label1.grid(row=1, column=0, sticky="w", padx=(60, 5), pady=15) #humidity
label2.grid(row=2, column=0, sticky="w", padx=(60, 5), pady=15) #time

val_temp.grid(row=0, column=1, sticky="w", pady=15)
val_hum.grid(row=1, column=1, sticky="w", pady=15)
val_time.grid(row=2, column=1, sticky="w", pady=15)

label4.grid(row=0, column=2, sticky="w", pady=15) #°C
label3.grid(row=1, column=2, sticky="w", pady=15) #%

root.mainloop()