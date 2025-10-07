from tkinter import *
from tkinter import ttk
 
def show_message():
    label["text"] = entry.get()

root = Tk()
root.title("Picrute info")     # заголовок окна
root.geometry("300x250")    # размеры окна
 
label = Label(text="Введите путь к картинке:") # текстовая метка
label.pack()

entry = ttk.Entry() # ввод
ttk.Entry().pack(anchor=NW, padx=8, pady= 8)

btn = ttk.Button(text="Enter", command=show_message) # кнопка enter
btn.pack(anchor=NW, padx=6, pady=6)
 
root.mainloop()
