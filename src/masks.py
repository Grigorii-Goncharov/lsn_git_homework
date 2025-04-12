import logging
import os

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../logs/masks.log")

# логер к текущему модулю
loger = logging.getLogger(__name__)
loger = logging.getLogger(__name__)
file_handler = logging.FileHandler(file_path, encoding = 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
loger.addHandler(file_handler)
loger.setLevel(logging.DEBUG)

# Настройка логгера

def get_mask_card_number(num_cart: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if not num_cart:
        loger.error('Получена пустая строка')
        raise ValueError("Номер карты не может быть пустым!")

    loger.info("проверяем карту")
    card_number = str(num_cart).replace(" ", "")
    loger.info("Проверяем длину карты на корректную длину")

    if len(card_number) != 16:
        loger.error(f'Некорректная длина номера карты: {len(card_number)}')
        raise ValueError("Введите 16-значный номер карты!")

    loger.info("Проверяем карту на числовое значение")
    if not card_number.isdigit():
        loger.error('Номер карты содержит нечисловые символы')
        raise ValueError("Введите числовое значение карты!")

    loger.info("Осуществляем вывод замаскированного номера карты")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    loger.info(f"Сгенерирована маскировка карты: {masked_card}")

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход н принимает на вход номер счета и возвращает его маску."""

    if not account_number:
        logger.error('Получена пустая строка в номере счета')
        raise ValueError("Номер счета не может быть пустым!")

    account_str = str(account_number).replace(" ", "")
    loger.info("Проверяем длину счёта на корректную длину")

    if len(account_str) != 20:
        logger.error(f'Некорректная длина счета: {len(account_str)}')
        raise ValueError("Номер счета должен состоять из 20 цифр!")

    loger.info("Проверяем номер счёта на числовое значение")
    if not account_str.isdigit():
        logger.error(f'Номер счета содержит нечисловые символы: {account_str}')
        raise ValueError("Номер счета должен содержать только цифры!")

    loger.info("Осуществляем вывод замаскированного номера карты")
    masked_account_number = f"**{account_str[-4:]}"
    loger.info(f"Сгенерирована маска счета: {masked_account_number}")

    return masked_account_number