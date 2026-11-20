import functools
import random

text = """Программирование помогает решать сложные задачи.
Python — простой и удобный язык программирования.
Изучение кода требует времени, практики и терпения.
Каждый день я пишу новый код и учусь.
Маленькие шаги ведут к большим результатам.
Программирование открывает новые возможности для работы и творчества."""
original_text = text


def create_replacer(old: str, new: str):
    #Преобразователь для замены слов
    def replacer(text):
        return text.replace(old, new)
    return replacer


def create_prefix_adder(prefix: str):
    #Преобразователь для добавления префикса в начало строк
    def prefix_adder(text):
        lines = text.splitlines()
        res = []
        for line in lines:
            res.append(prefix + line)
        result = '\n'.join(res)
        return result
    return prefix_adder


def create_word_filter(min_length: int):
    #Преобразователь для удаления слов по их длине
    def word_filter(text):
        lines = text.splitlines()
        result = []
        for line in lines:
            words = line.split()
            filtered_words = []
            for word in words:
                if len(word) >= min_length:
                    filtered_words.append(word)
            result.append(' '.join(filtered_words))
        return '\n'.join(result)
    return word_filter

def create_pipeline(funcs):
    #Функция вызова всех преобразователей
    def pipeline(text):
        for function in funcs:
            text = function(text)
        return text
    return pipeline

funcs = [create_replacer('Python', 'C++'), create_word_filter(3), create_prefix_adder('>>> ')]

pipeline = create_pipeline(funcs)
result = pipeline(text)
print('  ТЕКСТ ПОСЛЕ ПРИМЕНЕНИЯ ВСЕХ ПРЕОБРАЗОВАТЕЛЕЙ')
print(result)
print('-' * 20)

#===================================================================


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


@log_calls
def add(a, b):
    return a + b

print(add(10, 5))
print('-' * 20)


@count_calls
def greet(name):
    return f"Привет, {name}!"

print(' ВЫЗОВ ФУНКЦИИ С ПРИМЕНЕНИЕМ ДЕКОРАТОРОМ-СЧЁТЧИКОМ')
print(f'Результат первого применения: {greet("Мир")}') 
print(f'Результат второго применения: {greet("Python")}')
print(f'Результат третьего применения: {greet("Мир")}') 

print(f'Всего вызовов: {greet.call_count}') 
print('-' * 20)


@retry(times=3)
def unstable():
    if random.random() < 0.5:
        raise ValueError("Случайная ошибка!\n")
    return "Успех!\n"

print(' ВЫЗОВ ФУНКЦИИ С ДЕКОРАТОРОМ С ПАРАМЕТРОМ')
for i in range(5):
    try:
        print(f"Попытка {i+1}: {unstable()}")
    except ValueError as e:
        print(f"Попытка {i+1}: все 3 раза упали с ошибкой: {e}")
print('-' * 20)

#===================================================================


class Analyzer:

    def __init__(self, _data: str):
        self._data = _data
        self._history = []

    def __call__(self, transformer):
        self._data = transformer(self._data)
        self._history.append(transformer.__name__)
        return self._data

    def __len__(self):
        return len(self._data)

    def __str__(self):
        print('Красивое представление: ')
        if len(self._data) > 50:
            return self._data[:50] + '...'
        return self._data

    def history(self):
        return self._history


text = Analyzer(text)
text.__call__(create_prefix_adder('>>> '))
text.__call__(create_replacer('Python', 'C++'))
text.__call__(create_word_filter(3))

print(f' Список преобразователей, применённых к тексту:')
for i in text._history:
    print(i)

print()
print(text)
print('-'*20)

#===================================================================


class TextProcessor():

    def __init__(self, transformers: list):
        self.transformers = transformers

    def __len__(self):
        return len(self.transformers)

    def __iter__(self):
        return iter(self.transformers)

    def process(self, text):
        print(' ПРИМЕНЕНИЕ ВСЕХ ПРЕОБРАЗОВАТЕЛЕЙ К ТЕКСТУ\n')
        for transformer in self:
            text = transformer(text)
            print(f'Промежуточный результат: \n{text}\n')
        print(f"{'-' * 20}\nКонечный результат: \n{text}")


processor = TextProcessor(funcs)
processor.process(original_text)
















