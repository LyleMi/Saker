import os


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def hexdump(src, length=16, show=True):
    src = bytearray(src)
    result = []
    digits = 2

    for i in range(0, len(src), length):
        s = src[i: i + length]
        hexa = ' '.join(['%0*X' % (digits, x) for x in s])
        text = ''.join([chr(x) if 0x20 <= x < 0x7F else '.' for x in s])
        result.append(
            '%04X   %-*s   %s' %
            (i, length * (digits + 1), hexa, text)
        )
    if show:
        print('\n'.join(result))
    else:
        return '\n'.join(result)
