import os
from tkinter import messagebox

def rename_image(image_path: str, new_name: str, entry_path, entry_new_name, text_output):
    """Переименовывает изображение."""
    if not image_path:
        messagebox.showwarning("Ошибка", "Сначала выберите файл!")
        return

    if not new_name:
        messagebox.showwarning("Ошибка", "Введите новое имя файла!")
        return

    dir_path = os.path.dirname(image_path)
    ext = os.path.splitext(image_path)[1]
    new_path = os.path.join(dir_path, new_name + ext)

    if os.path.exists(new_path):
        messagebox.showerror("Ошибка", f"Файл с таким именем уже существует!")
        return

    try:
        os.rename(image_path, new_path)
        entry_path.delete(0, "end")
        entry_path.insert(0, new_path)
        entry_new_name.delete(0, "end")
        text_output.insert("end", f"Файл переименован в {new_name + ext}\n")
        messagebox.showinfo("Успех", f"Файл переименован в {new_name + ext}")
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))