import tkinter as tk
from tkinter import filedialog, messagebox
from image_info import get_image_info
from rename import rename_image

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

def handle_rename():
    image_path = entry_path.get()
    new_name = entry_new_name.get().strip()
    rename_image(image_path, new_name, entry_path, entry_new_name, text_output)

# GUI
root = tk.Tk()
root.title("Информация об изображении")
root.geometry("600x480")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entry_path = tk.Entry(frame_top, width=50)
entry_path.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame_top, text="Выбрать файл", command=choose_file)
btn_browse.pack(side=tk.LEFT)

btn_show = tk.Button(root, text="Показать информацию", command=show_info)
btn_show.pack(pady=10)

frame_rename = tk.Frame(root)
frame_rename.pack(pady=5)

entry_new_name = tk.Entry(frame_rename, width=30)
entry_new_name.pack(side=tk.LEFT, padx=5)

btn_rename = tk.Button(frame_rename, text="Переименовать картинку", command=handle_rename)
btn_rename.pack(side=tk.LEFT)

text_output = tk.Text(root, height=15, width=70)
text_output.pack(padx=10, pady=10)

root.mainloop()