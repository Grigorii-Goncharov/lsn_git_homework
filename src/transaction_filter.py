import re

def filter_transactions(transactions, search_string):
    """
     Функцию, которая принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка.
    """
    filtered_list_transactions = []

    pattern = re.compile(search_string, re.IGNORECASE)

    for transaction in transactions:
        description = transaction.get('description', '')
        if pattern.search(description):
            filtered_list_transactions.append(transaction)

    return filtered_list_transactions