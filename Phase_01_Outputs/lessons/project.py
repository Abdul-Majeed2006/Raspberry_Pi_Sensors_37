from machine import Pin, PWM
from time import sleep, sleep_ms
from sys import stdin
from uselect import poll

#Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', ' ': ' '}

pwm = PWM(Pin(16), freq = 1000, duty_u16 = 0)
poller = poll()
poller.register(stdin, 1)
current_message = 'sos'

def dot():
    pwm.duty_u16(32768)
    sleep_ms(100)
    pwm.duty_u16(65535)
    sleep_ms(300)

def dash():
    pwm.duty_u16(32768)
    sleep_ms(500)
    pwm.duty_u16(65535)
    sleep_ms(300)

def space():
    sleep_ms(1000)
    pwm.duty_u16(0)

def morse_code(message):
    for letter in message.upper():
        if poller.poll(0):
            return
        for k,v in morse_code_dict.items():
            if letter == k:
                for symbol in v:
                    if symbol == '.':
                        dot()
                    elif symbol == '-':
                        dash()
                    elif symbol == ' ':
                        space()
                space()

while 1:
    if poller.poll(0):
        current_message = stdin.readline().strip()
    print(f"Transmitting: {current_message}")
    morse_code(current_message)