from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    pairs = []

    if len(arr1) == 0 or len(arr2) == 0 or len(arr1) == 0 and len(arr2) == 0:
        return []
    else:
        for i in range(min(len(arr1), len(arr2))):
            pairs.append((arr1[i], arr2[i]))
        return pairs

# print(corresponding_pairs([], [3, 4]))
