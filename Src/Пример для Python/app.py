import os
import tkinter as tk
from tkinter import filedialog, messagebox
from image_info import get_image_info

def choose_file():
    file_path = filedialog.askopenfilename(
        title="Выберите изображение",
        filetypes=[("Изображения", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff")]
    )
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def show_info():
    image_path = entry_path.get()
    if not image_path:
        messagebox.showwarning("Ошибка", "Введите путь к изображению.")
        return
    try:
        info = get_image_info(image_path)
        text_output.delete(1.0, tk.END)
        for k, v in info.items():
            text_output.insert(tk.END, f"{k}: {v}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def rename_image():
    image_path = entry_path.get()
    new_name = entry_new_name.get().strip()
    
    if not image_path:
        messagebox.showwarning("Ошибка", "Сначала выберите файл!")
        return
    if not new_name:
        messagebox.showwarning("Ошибка", "Введите новое имя файла!")
        return
    
    # Получаем директорию и расширение старого файла
    dir_path = os.path.dirname(image_path)
    ext = os.path.splitext(image_path)[1]
    
    new_path = os.path.join(dir_path, new_name + ext)
    
    if os.path.exists(new_path):
        messagebox.showerror("Ошибка", "Файл с таким именем уже существует!")
        return
    
    try:
        os.rename(image_path, new_path)
        entry_path.delete(0, tk.END)
        entry_path.insert(0, new_path)
        messagebox.showinfo("Успех", f"Файл переименован в {new_name + ext}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создаём окно
root = tk.Tk()
root.title("Информация об изображении")
root.geometry("600x480")

# Поле для ввода пути
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entry_path = tk.Entry(frame_top, width=50)
entry_path.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame_top, text="Выбрать файл", command=choose_file)
btn_browse.pack(side=tk.LEFT)

# Кнопка для показа информации
btn_show = tk.Button(root, text="Показать информацию", command=show_info)
btn_show.pack(pady=10)

# Поле для переименования картинки
frame_rename = tk.Frame(root)
frame_rename.pack(pady=5)

entry_new_name = tk.Entry(frame_rename, width=30)
entry_new_name.pack(side=tk.LEFT, padx=5)

btn_rename = tk.Button(frame_rename, text="Переименовать картинку", command=rename_image)
btn_rename.pack(side=tk.LEFT)

# Поле вывода информации
text_output = tk.Text(root, height=15, width=70)
text_output.pack(padx=10, pady=10)

root.mainloop()

