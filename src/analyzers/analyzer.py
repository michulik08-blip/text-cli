
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
        if len(self._data) > 50:
            return self._data[:50] + '...'
        return self._data

    def history(self):
        return self._history