import functools

def log_calls(func):
    @functools.wraps(func)
    #декоратор, добавляющий вывод в консоль информации о функции
    def  wrapper(*args, **kwargs):
        print(f' ВЫЗОВ ФУНКЦИИ "{func.__name__}"\nАргументы: {args}')

        result = func(*args,**kwargs)

        print(f'Результат: {result}')
        return result
    return wrapper

def count_calls(func):
    #декоратор, считающий количество вызовов функции
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper

def retry(times=3):
    #Декторатор с параметром для перепроверки при запуске программы
    def retry_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            count = 1
            for attempt in range(times):
                print(f'Попытка вызова функции №{count}')
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
                

                count += 1
        return wrapper
    return retry_decorator