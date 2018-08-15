import sys
import os
import argparse
import curses

from sensoglove import SensoGlove

from signs.signs_bank import SignsBank
from signs.sign import Sign

parser = argparse.ArgumentParser()
parser.add_argument('host')
parser.add_argument('port', type=int)
parser.add_argument('file')
args = parser.parse_args()

def clear_line(scr, x):
    scr.move(x, 0)
    scr.clrtoeol()

def init_curses(scr, mode=True):
    if mode:
        curses.noecho()
    else:
        curses.echo()
    curses.curs_set(not mode)
    scr.nodelay(mode)

def input_sign(glove, scr):
    clear_line(scr, 3)
    hand = glove.hand
    init_curses(scr, False)
    scr.addstr(3, 0, 'Meaning:')
    meaning = scr.getstr(3, 9).decode('utf-8')
    init_curses(scr, True)
    clear_line(scr, 3)

    return Sign(hand, meaning)


def ncurses_loop(glove, sign_bank):
    scr = curses.initscr()
    init_curses(scr, True)

    scr.addstr(0, 0, '=== Signs Recorder ===')
    scr.addstr(1, 0, 'Commands | q: quit | r: record sign')
    while 1:
        glove.fetch_data()
        inputchar = scr.getch()
        if inputchar == ord('q'):
            break
        elif inputchar == ord('r'):
            sign = input_sign(glove, scr)
            sign_bank.add_sign(sign)
            scr.addstr(3, 0, 'The sign meaning \"' + sign.meaning + '\" has been successfully added to the sign bank')
    curses.endwin()


sign_bank = SignsBank()

if (os.path.exists(args.file)):
    sign_bank.load_from_file(args.file)

glove = SensoGlove(args.host, args.port)
try:
    glove.connect()
except Exception as e:
    print('Failed to connect with the glove: ', e)
    sys.exit(1)

ncurses_loop(glove, sign_bank)
sign_bank.dump_to_file(args.file)
