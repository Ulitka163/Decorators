from datetime import datetime


def logger(name_file):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            current_datetime = datetime.now()
            result = old_function(*args, **kwargs)
            _log = f'''
Вызвана функция: {old_function.__name__}
Время вызова функции: {current_datetime}
Аргументы функции: {args}, {kwargs}
Результат функции: {result}\n'''

            with open(name_file, 'a', encoding='UTF-8') as f:
                f.write(_log)
            return result
        return new_function
    return _logger


@logger(name_file='log.txt')
def foo():
    print('Привет мир!')


if __name__ == '__main__':
    foo()


