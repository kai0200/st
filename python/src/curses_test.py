# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()

    for i in range(0, 11):
        v = i - 10
        stdscr.addstr(i, 0, '10 divided by {} is {}').format(v, 10/v)

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
