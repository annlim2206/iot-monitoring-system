from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
#Настройка окна
root = Tk()
root.title("Iot-monitoring")
root.geometry("550x250")
root.resizable(False,False)
root.configure(bg='#f5badf')
icon = PhotoImage(file = "assets/icon.png")
root.iconphoto(False, icon)

#Размещение Gif
try:
    icon = PhotoImage(file="assets/icon.png")
    root.iconphoto(False, icon)
except Exception:
    print("Иконка окна не найдена.")
frames = []
desired_size = (60, 60)

try:
    with Image.open("assets/cat.gif") as pil_gif:
        for frame in ImageSequence.Iterator(pil_gif):
            resized_frame = frame.convert('RGBA').resize(desired_size, Image.Resampling.LANCZOS)
            frames.append(ImageTk.PhotoImage(resized_frame))
except FileNotFoundError:
    print("Файл assets/cat.gif не найден.")
except Exception as e:
    print(f"Ошибка при загрузке GIF: {e}")
def update_gif(ind):
    if frames:
        frame = frames[ind]
        ind += 1
        if ind == len(frames):
            ind = 0
        gif_label.configure(image=frame)
        root.after(300, update_gif, ind)
gif_label = Label(root, bg='#f5badf')
gif_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)
if frames:
    root.after(0, update_gif, 0)

#Размещение дополнительных изображений
try:
    fish_size = (70, 70)
    fish_pil_temp = Image.open("assets/fish.png").convert('RGBA').resize(fish_size, Image.Resampling.LANCZOS)
    fish_photo = ImageTk.PhotoImage(fish_pil_temp)
    fish_label = Label(root, image=fish_photo, bg='#f5badf')
    root.fish_photo = fish_photo
    fish_label.place(x=-5, y=-5, anchor="nw")

except FileNotFoundError:
    print("Файл assets/fish.png не найден.")
except Exception as e:
    print(f"Ошибка при загрузке PNG: {e}")

#Размещение текста
label = ttk.Label(text="temperature", font=("Times new roman", 23), background="#f5badf")
label1 = ttk.Label(text="humidity", font=("Times new roman", 23), background="#f5badf")
label2 = ttk.Label(text="date:", font=("Times new roman", 23), background="#f5badf")
label3 = ttk.Label(text="time:", font=("Times new roman", 23), background="#f5badf")
label4 = ttk.Label(text="%", font=("Times new roman", 23), background="#f5badf")
label5 = ttk.Label(text="°C", font=("Times new roman", 23), background="#f5badf")

val_temp = Label(root, text="--", font=("Times new roman", 23, "bold"), bg="#ffabe0")
val_hum = Label(root, text="--", font=("Times new roman", 23, "bold"), bg="#ffabe0")
val_date = Label(root, text="--.--.----", font=("Times new roman", 23, "bold"), bg="#ffabe0")
val_time = Label(root, text="--:--", font=("Times new roman", 23, "bold"), bg="#ffabe0")

#Размещение полученных значений
label.grid(row=0, column=0, sticky="w", padx=(40, 5), pady=15)  # temperature
label1.grid(row=1, column=0, sticky="w", padx=(40, 5), pady=15) # humidity
label2.grid(row=2, column=0, sticky="w", padx=(40, 5), pady=15) # date:

val_temp.grid(row=0, column=1, sticky="w", padx=5, pady=15)
val_hum.grid(row=1, column=1, sticky="w", padx=5, pady=15)
val_date.grid(row=2, column=1, sticky="w", padx=5, pady=15)

label5.grid(row=0, column=2, sticky="w", padx=5, pady=15) #°C
label4.grid(row=1, column=2, sticky="w", padx=5, pady=15) #%
label3.grid(row=2, column=2, sticky="w", padx=(20, 5), pady=15)
val_time.grid(row=2, column=3, sticky="w", padx=5, pady=15)

root.mainloop()