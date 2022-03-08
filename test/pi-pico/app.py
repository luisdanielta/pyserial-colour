import random
import time

id = ['R:', 'G:', 'B:']

c = 0
while True:
    number = random.randint(0, 255)
    print(id[c], number)
    time.sleep_ms(500)
    c += 1
    if c == 3:
        c = 0
