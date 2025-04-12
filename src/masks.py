import logging
import os

# # Получаем путь к текущему скрипту
# script_dir = os.path.dirname(os.path.abspath(__file__))
#
# # Определяем путь к файлу относительно текущего скрипта
# file_path = os.path.join(script_dir, "../logs/masks.log")

# логгер к текущему модулю
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs", "masks.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(num_cart: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    if not num_cart:
        logger.error('Получена пустая строка')
        raise ValueError("Номер карты не может быть пустым!")

    logger.info("проверяем карту")
    card_number = str(num_cart).replace(" ", "")
    logger.info("Проверяем длину карты на корректную длину")

    if len(card_number) != 16:
        loger.error(f'Некорректная длина номера карты: {len(card_number)}')
        raise ValueError("Введите 16-значный номер карты!")

    logger.info("Проверяем карту на числовое значение")
    if not card_number.isdigit():
        loger.error('Номер карты содержит нечисловые символы')
        raise ValueError("Введите числовое значение карты!")

    logger.info("Осуществляем вывод замаскированного номера карты")
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Сгенерирована маскировка карты: {masked_card}")

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход н принимает на вход номер счета и возвращает его маску."""

    if not account_number:
        logger.error('Получена пустая строка в номере счета')
        raise ValueError("Номер счета не может быть пустым!")

    account_str = str(account_number).replace(" ", "")
    logger.info("Проверяем длину счёта на корректную длину")

    if len(account_str) != 20:
        logger.error(f'Некорректная длина счета: {len(account_str)}')
        raise ValueError("Номер счета должен состоять из 20 цифр!")

    logger.info("Проверяем номер счёта на числовое значение")
    if not account_str.isdigit():
        logger.error(f'Номер счета содержит нечисловые символы: {account_str}')
        raise ValueError("Номер счета должен содержать только цифры!")

    logger.info("Осуществляем вывод замаскированного номера карты")
    masked_account_number = f"**{account_str[-4:]}"
    logger.info(f"Сгенерирована маска счета: {masked_account_number}")

    return masked_account_number