import os
import random

while(True):
    print("\033[{0}m\033[{1}m{2}".format(random.randint(30, 37), random.randint(40, 47), 
    "xxxxxxxxxx     xxxxxxxxxx     xx    xx     xxxxxxxxxx     xxxxxxxxxx\n    xx         xx             xx   xx      xx                 xx    \n    xx         xxxxxxx        xx xx        xx                 xx    \n    xx         xx             xx x         xx                 xx    \n    xx         xx             xx xx        xx                 xx    \n    xx         xxxxxxxxxx     xx   xxx     xxxxxxxxxx         xx    \n"))
    os.system('cls')