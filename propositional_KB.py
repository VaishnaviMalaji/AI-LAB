
import itertools
import re

def tokenize(expr):
    pattern = r'<->|->|[()]|[A-Za-z_][A-Za-z0-9_]*'
    tokens = re.findall(pattern, expr)

    result = []
    for t in tokens:
        t = t.upper()

        if t in ("AND", "OR", "NOT", "IFF", "IMPLIES"):
            result.append(t)
        elif t == "->":
            result.append("IMPLIES")
        elif t == "<->":
            result.append("IFF")
        elif t == "(" or t == ")":
            result.append(t)
        else:
            result.append(t)

    return result


def evaluate(expr, values):
    tokens = tokenize(expr)
    pos = 0

    def atom():
        nonlocal pos

        if pos >= len(tokens):
            raise ValueError("Invalid expression")

        if tokens[pos] == "NOT":
            pos += 1
            return not atom()

        if tokens[pos] == "(":
            pos += 1
            result = parse_iff()

            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError("Missing closing bracket")

            pos += 1
            return result

        name = tokens[pos]
        pos += 1
        return values[name]

    def parse_and():
        nonlocal pos
        result = atom()

        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            right = atom()
            result = result and right

        return result

    def parse_or():
        nonlocal pos
        result = parse_and()

        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            right = parse_and()
            result = result or right

        return result

    def parse_implies():
        nonlocal pos
        result = parse_or()

        if pos < len(tokens) and tokens[pos] == "IMPLIES":
            pos += 1
            right = parse_implies()
            return (not result) or right

        return result

    def parse_iff():
        nonlocal pos
        result = parse_implies()

        while pos < len(tokens) and tokens[pos] == "IFF":
            pos += 1
            right = parse_implies()
            result = result == right

        return result

    answer = parse_iff()

    if pos != len(tokens):
        raise ValueError("Invalid expression")

    return answer


def check_entailment(kb, query):
    operators = {"AND", "OR", "NOT", "IFF", "IMPLIES"}

    symbols = sorted({
        token
        for expr in kb + [query]
        for token in tokenize(expr)
        if token not in operators and token not in ("(", ")")
    })

    for combination in itertools.product(
        [False, True], repeat=len(symbols)
    ):
        assignment = dict(zip(symbols, combination))

        kb_true = all(
            evaluate(statement, assignment)
            for statement in kb
        )

        if kb_true and not evaluate(query, assignment):
            print("\nNOT ENTAILED")
            print("Counterexample:")

            for symbol in symbols:
                value = "TRUE" if assignment[symbol] else "FALSE"
                print(symbol, "=", value)

            return

    print("\nENTAILED")


# Main program
print("PROPOSITIONAL KNOWLEDGE BASE")

n = int(input("Enter number of KB statements: "))

kb = []

for i in range(n):
    statement = input("Enter KB statement " + str(i + 1) + ": ")
    kb.append(statement)

query = input("Enter query: ")

check_entailment(kb, query)
