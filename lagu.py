from time import sleep
import sys

def print_lyrics():
    lines = [
        ("dan jantungku terus memanggil indah namamu", 0.08),
        ("takkan pernah hati ini mendua", 0.07),
        ("sampai akhir, sampai akhir", 0.07),
        ("hidup ini", 0.07),
        ("sampai akhir, sampai akhir", 0.08),
        ("hidup ini", 0.06),
    ]
    delays = [4, 3, 2.5, 5, 7, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print('')

print_lyrics()