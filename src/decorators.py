from functools import wraps


def log(filename=None):
    """Декоратор, логирующий выполнение функций"""

    def wrapper(func):
        """Обёртка функции"""

        @wraps(func)
        def inner(*args, **kwargs):
            """Функиия, ведущая запись лога"""
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f'\n{func.__name__} started Ok. with Inputs: {args}, {kwargs}.\n{func.__name__} finished at result {func(*args, **kwargs)}.')
                else:
                    print(
                        f'\n{func.__name__} started Ok. with Inputs: {args}, {kwargs}.\n{func.__name__} finished at result {func(*args, **kwargs)}.')
                return result
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f'{func.__name__} ошибка: {error}. Inputs: {args}, {kwargs}')
                else:
                    print(f'{func.__name__} ok. Inputs:{args}, {kwargs}')

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
