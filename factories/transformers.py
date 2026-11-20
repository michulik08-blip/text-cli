#Замыкания

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