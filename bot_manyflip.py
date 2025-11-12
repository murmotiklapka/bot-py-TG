import random

def many_flip():
    site_nom = random.randint(1,2)
    if site_nom == 1:
        site = "орёл"
    elif site_nom == 2:
        site = "решка"
    return site