#!/usr/bin/python3
"""
Модуль мычания.
"""

import morse
import curses


def moo(oos=2, end=""):
    """
    Издать мычание длиной oos с end в конце.

    :param oos: Количество 'o'
    :param end: Символ в конце мычания
    """

    return "M" + "o" * int(oos) + end


def moorse(text, dit=2, dah=3, pause=" ", space="  ", sep="\n"):
    r"""
    Промычать азбукой морзе текст на английском.

    :param text: Текст для мычания
    :param dit: Количесвто 'o' в точке (2)
    :param dah: Количество 'o' в тире (3)
    :param pause: Заполнитель между сигналами (" ")
    :param space: Заполнитель между буквами ("  ")
    :param sep: Заполнитель между словами ("\\n")
    """

    return sep.join(
        space.join(
            pause.join(moo(dit if c == '.' else dah) for c in letter)
            for letter in morse.string_to_morse(word))
        for word in text.split())


def _curses_main(stdscr, res):
    stdscr.box()
    H, W = stdscr.getmaxyx()
    S = res.split('\n')
    N = (H - len(S)) // 2
    for i, line in enumerate(S):
        stdscr.addstr(N + i, (W - len(line)) // 2, line)
    stdscr.getch()


def coorse(*args, **kwargs):
    """Помычать красиво! Параметры — такие же как у :py:func:`moorse`."""
    curses.wrapper(_curses_main, moorse(*args, **kwargs))


if __name__ == "__main__":  # pragma: no cover
    import sys
    if len(sys.argv) > 1:
        if "" in sys.argv:
            coorse(*sys.argv[1:])
        else:
            print(moorse(*sys.argv[1:]))
    else:
        print(moorse("Hello , world !"))