#!/usr/bin/env python3
import argparse
import sys
from random import seed, randint  #, random as rand

ABOUT = """
Ensemencer esointerpreter

"""


def read():
    """Read (psuedo-random) data.."""
    i = randint(0, 255)
    #i = int(rand() * 256)
    if debug:
        print('READ:', i)
    return i


def readinput(inbuffer):
    if inbuffer:
        return inbuffer.pop(0)
    return ord(sys.stdin.read(1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=ABOUT)
    parser.add_argument('--input', '-i', help='list (comma separated) list of initial input values')
    parser.add_argument('--debug', '-d', help='turn on debug output', action='store_true')
    parser.add_argument('file', help='source file to process')
    args = parser.parse_args()

    inbuffer = []

    debug = args.debug
    if args.input:
        inbuffer += [int(v) for v in args.input.split(',')]

    if debug:
        print('INPUT BUFFER', inbuffer)

    current_seed = 0
    seed(0, version=2)  # initialise twister to 0
    digits = ''
    with open(args.file, 'r') as f:
        c = f.read(1)
        while True:
            if digits and c not in '0123456789':
                for i in range(int(digits)):
                    read()
                digits = ''

            if not c or c == '-':
                if debug:
                    print('END OF FILE!')
                f.seek(0)
                seed(current_seed)
            elif c in '0123456789':
                digits += c
            elif c == '!':
                break
            elif c == '.':
                out = read()
                if debug:
                    print('OUTPUT:', out)
                print(chr(out), end='', flush=True)
            elif c == '#':
                current_seed = readinput(inbuffer)
                if debug:
                    print('INPUT:', current_seed)
                seed(current_seed)
            elif c == '<':  # insert random int to inbuffer
                inbuffer.insert(0, read()) 
            elif c == '>':  # append random int to inbuffer
                inbuffer.append(read())
            elif c == '?':
                if read() & 1:
                    f.read(1)  # skip next instruction byte
            c = f.read(1)
