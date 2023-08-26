__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds % 86400 % 3600 % 60 % 60 < 10:
        sec = '0' + str(seconds % 86400 % 3600 % 60 % 60) + 's'
    else:
        sec = str(seconds % 86400 % 3600 % 60 % 60) + 's'
    if seconds % 86400 % 3600 // 60 < 10:
        mins = '0' + str(seconds % 86400 % 3600 // 60) + 'm'
    else:
        mins = str(seconds % 86400 % 3600 // 60) + 'm'
    if seconds % 86400 // 3600 < 10:
        hours = '0' + str(seconds % 86400 // 3600) + 'h'
    else:
        hours = str(seconds % 86400 // 3600) + 'h'
    if seconds // 86400 < 10:
        sut = '0' + str(seconds // 86400) + 'd'
    else:
        sut = str(seconds // 86400) + 'd'

    if sut == '00d':
        if hours == '00h':
            if mins == '00m':
                return sec
            return mins + sec
        return hours + mins + sec
    return sut + hours + mins + sec


# print(seconds_to_str(1))
