import os
from datetime import datetime
from PIL import Image

def get_image_info(image_path: str) -> dict:
    """Возвращает информацию о картинке."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл '{image_path}' не найден")

    file_size = os.path.getsize(image_path)
    creation_time = os.path.getctime(image_path)
    creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")

    with Image.open(image_path) as img:
        width, height = img.size
        format = img.format

    return {
        "Путь": image_path,
        "Формат": format,
        "Разрешение": f"{width}x{height}",
        "Ширина": width,
        "Высота": height,
        "Дата создания": creation_date
    }