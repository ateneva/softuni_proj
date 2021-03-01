
from pyfiglet import figlet_format

def print_art(msg):
    art = figlet_format(msg)
    print(art)

print_art(input())
