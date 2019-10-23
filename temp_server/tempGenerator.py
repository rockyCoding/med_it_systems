from random import random, uniform, randint

MIN_TEMP = 17.5
MAX_TEMP = 22.5


def startTempGenerator():
    return round(uniform(MIN_TEMP, MAX_TEMP), 1)


def tempGenerator(prevTemp):
    operator = randint(0, 1)
    if random() > 0.2:
        diff = 0.1
    else:
        diff = 0.2
    if operator == 0:
        newTemp = prevTemp - diff
        if newTemp < MIN_TEMP:
            return  prevTemp + diff
        else:
            return newTemp
    else:
        newTemp = prevTemp + diff
        if newTemp > MAX_TEMP:
            return prevTemp - diff
        else:
            return newTemp