import time, sys, random

def slow(text, speed = 60):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1/speed)
    print()
    time.sleep((1/speed)*2)

def slow_input(text, speed = 60):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1/speed)
    string = input()
    if string == "exit":
        exit()
    return string

def choice(choices, text="Hva gjør du?", speed = 60):
    slow(text, speed)
    string = "Alternativer: "
    for i, choice in enumerate(choices):
        string += f"{choice} ({i+1}), "
    slow(string[:len(string)-2], speed)
    choice = 0
    string = slow_input("> ", speed)
    while True:
        try:
            choice = int(string)
            if choice < 1 or choice > len(choices):
                continue
        except:
            continue
        break
    return choice-1

def range_input(start, end, text="> ", is_float = True, speed = 60):
    num = 0
    string = slow_input(text)
    while True:
        try:
            if is_float:
                num = float(string)
            else:
                num = int(string)
            if num < start or num > end:
                continue
        except:
            continue
        break
    return round(num, 1)

def random_choice(probabilities):
    prob = probabilities
    if type(probabilities[0]) == list or type(probabilities[0]) == tuple:
        prob = [i[0] for i in probabilities]
    total = sum(prob)
    normalized = [i/total for i in prob]
    rand = random.random()
    i = 0
    while rand > 0:
        rand -= normalized[i]
        i += 1
    if type(probabilities[0]) == list or type(probabilities[0]) == tuple:
        return probabilities[i-1][1]
    return i-1