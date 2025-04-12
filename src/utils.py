import json
import os
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs", "utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_file(filename=None):
    """Функция для чтения JSON-файла и обработки возможных ошибок при его открытии и чтении"""

    try:
        logger.info("Читаем JSON файл")
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            logger.info(f"Данные в файле {data} не являются списком")
            return []

        logger.info("Файл успешно прочитан")
        return data

    except FileNotFoundError:
        logger.error(f'Файл не найден по пути: {filename}')
        print(f"Файл не найден по пути: {filename}")
        return []

    except json.JSONDecodeError:
        logger.error(f'Ошибка при декодировании JSON из файла: {filename}')
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []
