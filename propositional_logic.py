
import re

def tokenize(expr):
    return re.findall(r'<->|->|[()]|[A-Za-z_]\w*', expr.upper())


def parse(expr):
    tokens = tokenize(expr)
    pos = 0

    def atom():
        nonlocal pos

        if pos >= len(tokens):
            raise ValueError("Invalid expression")

        if tokens[pos] == "NOT":
            pos += 1
            return ("NOT", atom())

        if tokens[pos] == "(":
            pos += 1
            result = iff()

            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError("Missing closing bracket")

            pos += 1
            return result

        name = tokens[pos]
        pos += 1

        if name in ("AND", "OR", "NOT", "IMPLIES", "IFF"):
            raise ValueError("Invalid expression")

        return ("VAR", name)

    def conjunction():
        nonlocal pos
        result = atom()

        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            result = ("AND", result, atom())

        return result

    def disjunction():
        nonlocal pos
        result = conjunction()

        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            result = ("OR", result, conjunction())

        return result

    def implication():
        nonlocal pos
        result = disjunction()

        if pos < len(tokens) and tokens[pos] == "->":
            pos += 1
            result = ("IMPLIES", result, implication())

        return result

    def iff():
        nonlocal pos
        result = implication()

        while pos < len(tokens) and tokens[pos] == "<->":
            pos += 1
            result = ("IFF", result, implication())

        return result

    result = iff()

    if pos != len(tokens):
        raise ValueError("Invalid expression")

    return result


def eliminate(expr):
    op = expr[0]

    if op == "VAR":
        return expr

    if op == "NOT":
        return ("NOT", eliminate(expr[1]))

    a = eliminate(expr[1])
    b = eliminate(expr[2])

    if op == "IMPLIES":
        return ("OR", ("NOT", a), b)

    if op == "IFF":
        return (
            "AND",
            ("OR", ("NOT", a), b),
            ("OR", ("NOT", b), a)
        )

    return (op, a, b)


def nnf(expr, neg=False):
    op = expr[0]

    if op == "VAR":
        return ("NOT", expr) if neg else expr

    if op == "NOT":
        return nnf(expr[1], not neg)

    if op == "AND":
        new_op = "OR" if neg else "AND"
        return (new_op, nnf(expr[1], neg),
                nnf(expr[2], neg))

    if op == "OR":
        new_op = "AND" if neg else "OR"
        return (new_op, nnf(expr[1], neg),
                nnf(expr[2], neg))


def cnf(expr):
    if expr[0] == "VAR":
        return [frozenset([(expr[1], True)])]

    if expr[0] == "NOT":
        return [frozenset([(expr[1][1], False)])]

    left = cnf(expr[1])
    right = cnf(expr[2])

    if expr[0] == "AND":
        return left + right

    result = []

    for c1 in left:
        for c2 in right:
            clause = c1 | c2

            if not any((name, not sign) in clause
                       for name, sign in clause):
                result.append(clause)

    return result


def resolution(kb, query):
    clauses = set()

    for statement in kb:
        tree = parse(statement)
        tree = eliminate(tree)
        tree = nnf(tree)
        clauses.update(cnf(tree))

    query_tree = parse(query)
    negated = nnf(query_tree, True)
    clauses.update(cnf(negated))

    while True:
        new_clauses = set()
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                c1 = clause_list[i]
                c2 = clause_list[j]

                for literal in c1:
                    name, sign = literal
                    opposite = (name, not sign)

                    if opposite in c2:
                        resolvent = (c1 - {literal}) | (
                            c2 - {opposite}
                        )

                        tautology = any(
                            (s, not v) in resolvent
                            for s, v in resolvent
                        )

                        if not tautology:
                            if not resolvent:
                                print("PROVED")
                                return

                            if resolvent not in clauses:
                                new_clauses.add(resolvent)

        if not new_clauses:
            print("NOT PROVED")
            return

        clauses.update(new_clauses)


# Main program
print("PROPOSITIONAL LOGIC - RESOLUTION")

n = int(input("Enter number of KB statements: "))

kb = []

for i in range(n):
    statement = input("Enter KB statement " + str(i + 1) + ": ")
    kb.append(statement)

query = input("Enter query: ")

resolution(kb, query)
