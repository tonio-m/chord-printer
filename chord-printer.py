#!/bin/python
# python chord-printer.py "Dmin7, Cmaj7, Fmaj7, Amin7"

import re
import argparse
from sys import argv
from itertools import chain


CHORD_TYPES = {
    'maj7': lambda x: [x,x+4,x+7,x+11], 
    '7': lambda x: [x,x+4,x+7,x+10],
    'min7': lambda x: [x,x+3,x+7,x+10],
    'min7b5': lambda x: [x,x+3,x+6,x+10],
    'dim7': lambda x: [x,x+3,x+6,x+9],
}

NOTE_ENUM = {
    'c': 0,
    'c#': 1,
    'db': 1,
    'd': 2,
    'd#': 3,
    'eb': 3,
    'e': 4,
    'f': 5,
    'f#': 6,
    'gb': 6,
    'g': 7,
    'g#': 8,
    'ab': 8,
    'a': 9,
    'a#': 10,
    'bb': 10,
    'b': 11,
    'cb': 11,
} 

NOTE_ENUM_BACKWARDS = ['c','c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

OCTAVE_DRAWING = """
  |1| |3|  |  |6| |8| |a|  |
  |1| |3|  |  |6| |8| |a|  |
  |1| |3|  |  |6| |8| |a|  |
  |_| |_|  |  |_| |_| |_|  |
000|222|444|555|777|999|bbb|
000|222|444|555|777|999|bbb|
___|___|___|___|___|___|___|
"""


def concatenate_octave_drawings(*drawings):
    drawings_lines = [drawing.split('\n') for drawing in drawings]

    d = [''.join(list(chain(*same_line_strings))) for same_line_strings in list(zip(*drawings_lines))]
    return '\n'.join(d)


def parse_chord(string):
    match = re.match('(^[A-Za-z]#?b?)(.*)$',string)
    note_string = match[1].lower()
    chord_type = match[2].lower()

    note = NOTE_ENUM[note_string]
    chord_note_numbers = CHORD_TYPES[chord_type](note)
    return chord_note_numbers


def paint_octave_drawing(chord):
    drawing = OCTAVE_DRAWING
    for i in range(0,12):
        hex_placeholder = format(i,'x')
        if i in chord:
            drawing = drawing.replace(hex_placeholder,'X')
        else:
            drawing = drawing.replace(hex_placeholder,' ')
    return drawing

def paint_chord(chord):
    first_octave = [i for i in chord if i < 12]
    second_octave = [i % 12 for i in chord if i >= 12]

    first_drawing = paint_octave_drawing(first_octave)
    second_drawing = paint_octave_drawing(second_octave)
    return concatenate_octave_drawings(first_drawing,second_drawing)


def get_notes_strings(notes):
    return [NOTE_ENUM_BACKWARDS[note % 12] for note in notes]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Prints the notes of a chord')

    parser.add_argument('chords', type=str, help='Chords to print')
    parser.add_argument('--notes', action='store_true', help='Print the notes instead of drawing the chords')

    args = parser.parse_args()
    chords_string = args.chords.replace('♭','b')
    chords = [s.strip() for s in chords_string.split(',')]

    for chord in chords:
        print(chord,end=': ')

        chord_notes = parse_chord(chord)
        if args.notes:
            notes = get_notes_strings(chord_notes)
            print(' '.join(notes))
        else:
            chord_drawing = paint_chord(chord_notes)
            print(chord_drawing)