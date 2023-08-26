from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = text.split()

    if len(words) == 0:
        return (None, None)

    minWord = maxWord = words[0]

    for word in words:
        if len(word) < len(minWord):
            minWord = word
        if len(word) > len(maxWord):
            maxWord = word

    if minWord == maxWord:
        return (None, maxWord)
    if minWord == '' and maxWord == '':
        return (None, None)
    elif minWord == '' and maxWord != '':
        return (None, maxWord)
    elif minWord != '' and maxWord == '':
        return (minWord, None)
    else:
        return (minWord, maxWord)


# print(find_shortest_longest_word('           '))
