import random

def gen_pass():
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    e = random.randint(1,20)
    for nompass in range(e):
        password += random.choice(elements)
    return password
    