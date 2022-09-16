import sympy

def geometric(numbers, symbol):
    """
    geometric finner den eksplisitte formelen for tallfølgen bestående av numbers.

    Formelen er skrevet på formen: a*(b**n)+c, hvor n er indeksen. 
    Første element er n=1, andre element er n=2 osv.

    Formelen blir returnet som sympy-formel, hvor n i formelen er byttet ut med symbol
    """
    sympy.Symbol
    if len(numbers) < 3:
        return None
    factor = None
    for i in range(len(numbers)-2):
        diff1 = numbers[i+1] - numbers[i]
        diff2 = numbers[i+2] - numbers[i+1]
        if diff1 == 0 or diff2 == 0:
            return None
        current_factor = diff2 / diff1
        if factor != None and factor != current_factor:
            return None
        factor = current_factor

    shift = (numbers[1] - numbers[0] * factor) / (1 - factor)
    mul = (numbers[0] - shift) / factor

    return mul * factor**symbol + shift


def arithmetic(numbers, symbol):
    d = depth(numbers)
    s = sympy.symbols(f"a:{d+1}")
    equations = []
    for i in range(1, d+2):
        equation = 0
        for j in range(d+1):
            equation += s[j] * (i**j)
        equations.append(sympy.Eq(equation, numbers[i-1]))
    constants = list(sympy.solve(equations).values())
    return sum([constants[i] * symbol**i for i in range(d+1)])

def depth(numbers, current_depth=0):
    current_diff = None
    valid = True
    for num in numbers:
        if current_diff != None and num != current_diff:
            valid = False
            break
        current_diff = num
    
    if valid:
        return current_depth

    new_numbers = []
    for i in range(len(numbers) - 1):
        new_numbers.append(numbers[i+1] - numbers[i])
    return depth(new_numbers, current_depth+1)

def auto(numbers, symbol):
    exp = geometric(numbers, symbol)
    if exp != None and exp != sympy.nan:
        return exp
    return arithmetic(numbers, symbol)

def parse_input(user_input):
    user_input = user_input.replace(" ", "")
    strings = user_input.split(",")
    numbers = []
    for string in strings:
        try:
            numbers.append(sympy.parsing.sympy_parser.parse_expr(string))
        except:
            return None
    return numbers

def print_values(user_input, last_formula, symbol):
    if len(user_input) < 3:
        return None
    if user_input[:2] != "n=":
        return None
    num = user_input[2:]
    values = []
    if ":" in num:
        parts = num.split(":")
        if len(parts) != 2:
            return None
        if not is_number(parts[0]) or not is_number(parts[1]):
            return None
        start = int(parts[0])
        end = int(parts[1])
        dir = int((end-start)/abs(end-start))
        values = list(range(start, end+dir, dir))
    else:
        if not is_number(num):
            return None
        values.append(int(num))
    for n in values:
        print(f"{n}:\t{last_formula.subs(symbol, n)}")
    return True

def is_number(number):
    if len(number) == 0:
        return False
    if number.isnumeric():
        return True
    if number[0] == "-" and number[1:len(number)].isdigit():
        return True
    return False

def main():
    last_formula = None
    symbol = sympy.Symbol("n")
    while True:
        user_input = input("> ")
        if user_input == "exit" or user_input == "e":
            break
        if user_input == "pretty" or user_input == "p":
            if last_formula == None:
                print("No formula")
                continue
            sympy.pretty_print(last_formula)
            continue
        if user_input == "latex" or user_input == "l":
            if last_formula == None:
                print("No formula")
                continue
            sympy.print_latex(last_formula)
            continue
        if print_values(user_input, last_formula, symbol) != None:
            continue

        numbers = parse_input(user_input)
        if numbers == None:
            print("Invalid input")
            continue
        formula = auto(numbers, symbol)
        if formula == None:
            print("No formula found")
            continue
        last_formula = formula
        print(formula)

if __name__ == "__main__":
    main()