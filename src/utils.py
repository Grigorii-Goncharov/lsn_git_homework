import logging
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../logs/utils.log")

# логер к текущему модулю
loger = logging.getLogger(__name__)
file_handler = logging.FileHandler(file_path, encoding = 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
loger.addHandler(file_handler)
loger.setLevel(logging.DEBUG)

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../data/operations.json")


def read_file(filename=None):
    """Функция для чтения JSON-файла и обработки возможных ошибок при его открытии и чтении"""

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            return []

        return data
    except FileNotFoundError:
        print(f"Файл не найден по пути: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []
