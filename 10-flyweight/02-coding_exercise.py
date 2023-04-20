# You are given a class called Sentence , which takes a string such as 'hello world'.
# You need to provide an interface such that the indexer returns a flyweight that can
# be used to capitalize a particular word in the sentence.

# Typical use would be something like:

# sentence = Sentence('hello world')
# sentence[1].capitalize = True
# print(sentence)  # writes "hello WORLD"

class Sentence:
    class Word:
        def __init__(self, text: str, pos: int, capitalize=False) -> None:
            self._text = text
            self._pos = pos
            self.capitalize = capitalize
    
    def __init__(self, plain_text):
        self.splitted_text = plain_text.split(" ")
        self._words = {}

    def __getitem__(self, pos):
        self._words[pos] = self.Word(text=self.splitted_text[pos],
                                     pos=pos)
        return self._words[pos]

    def __str__(self) -> str:
        result = []
        for pos, wrd in enumerate(self.splitted_text):
            w = wrd
            if pos in self._words:
                w = w.upper() if self._words[pos].capitalize else w
            result.append(w)
        return ' '.join(result)


if __name__ == "__main__":
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"
    
