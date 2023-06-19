from typing import Iterable, Annotated

class Character:
    def __init__(self, char: Annotated[str, "Sequence of 1 or more chars to represent one language character"]):
        self.value = char
    
    def __str__(self) -> str:
        if len(self.value) > 1:
            return f'\[{self.value}]'
        
        return self.value

class Alphabet:
    def __init__(self, character_set: Iterable[Character]):
        self.value = character_set
    
    def __str__(self) -> str:
        return (
                f"["
                f"{', '.join(map(str, self.value))}"
                f']'
            )

class Word:
    def __init__(self, word: Iterable[Character]):
        self.value = word

    def __str__(self) -> str:
        return ''.join(map(str, self.value))

class Language:
    def __init__(self, word_set: Iterable[Word], alphabet: Alphabet):
        self.alphabet = alphabet
        self.words = word_set

class DFA:
    def __init__(self):
        pass