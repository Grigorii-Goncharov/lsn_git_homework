import csv
from typing import Any, Dict, List

import pandas as pd

def read_csv_file(file_path: str, delimiter: str = ";") -> List[Dict]:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден!")
            return []
        except Exception as e:
            print(f"Ошибка при чтении CSV: {e}")
            return []

def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """Функция для считывания финансовых операций из XLSX-файла и возврата списка словарей."""
    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей (по одному на строку)
        transaction_list = df.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        print(f"Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []
