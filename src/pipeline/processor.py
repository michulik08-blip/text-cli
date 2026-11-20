
class TextProcessor():

    def __init__(self, transformers: list):
        self.transformers = transformers

    def __len__(self):
        return len(self.transformers)

    def __iter__(self):
        return iter(self.transformers)

    def process(self, text, on_step=None):
        """Применяет все преобразователи по очереди и возвращает итоговый текст."""
        for transformer in self:
            text = transformer(text)
            if on_step is not None:
                on_step(transformer, text)
        return text