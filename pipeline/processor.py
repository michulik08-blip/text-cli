
class TextProcessor():

    def __init__(self, transformers: list):
        self.transformers = transformers

    def __len__(self):
        return len(self.transformers)

    def __iter__(self):
        return iter(self.transformers)

    def process(self, text):
        for transformer in self:
            text = transformer(text)
        return text