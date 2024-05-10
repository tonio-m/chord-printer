# chord-printer

## Usage:
It's as simple as this:
```
$ python chord-printer.py 'Dmin7, Cmaj7, Fmaj7, Amin7'
Dmin7

  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
   |XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |   |   |
   |XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |   |   |
___|___|___|___|___|___|___|___|___|___|___|___|___|___|

Cmaj7

  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |   |   |   |
XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |   |   |   |
___|___|___|___|___|___|___|___|___|___|___|___|___|___|

Fmaj7

  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
   |   |   |XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |
   |   |   |XXX|   |XXX|   |XXX|   |XXX|   |   |   |   |
___|___|___|___|___|___|___|___|___|___|___|___|___|___|

Amin7

  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
   |   |   |   |   |XXX|   |XXX|   |XXX|   |XXX|   |   |
   |   |   |   |   |XXX|   |XXX|   |XXX|   |XXX|   |   |
___|___|___|___|___|___|___|___|___|___|___|___|___|___|
```

you can also do this:
```
$ python chord-printer.py --notes "Dmin7, Cmaj7, Fmaj7, Amin7"
Dmin7: d f a c
Cmaj7: c e g b
Fmaj7: f a c e
Amin7: a c e g
```

Try it yourself:
```
# TYLER THE CREATOR - BEST INTEREST
python chord-printer.py --notes "Gbmaj7, Ebmin7, Fmin7, Abmin7"
Gbmaj7: f# a# c# f
Ebmin7: d# f# a# c#
Fmin7: f g# c d#
Abmin7: g# b d# f#

# DJAVAN - SAMURAI
python chord-printer.py --notes "emaj7, gdim7, g#min7, c#maj7, bmaj7"
emaj7: e g# b d#
gdim7: g a# c# e
g#min7: g# b d# f#
c#maj7: c# f g# c
bmaj7: b d# f# a#
```