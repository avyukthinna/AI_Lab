def is_variable(x):
    """Check if x is a variable."""
    return isinstance(x, str) and x[0].islower()

def unify(x, y, subst):
    """Unify two terms x and y under a given substitution subst."""
    print(f"Comparing: {x} with {y}")
    if subst is None:
        return None
    elif x == y:
        print(f"Both are equal: {x} == {y}")
        return subst
    elif is_variable(x):
        return unify_variable(x, y, subst)
    elif is_variable(y):
        return unify_variable(y, x, subst)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst
    else:
        print(f"Cannot unify {x} and {y}")
        return None

def unify_variable(var, x, subst):
    """Handle variable unification."""
    if var in subst:
        print(f"Variable {var} is already in substitution. Resolving with {subst[var]}.")
        return unify(subst[var], x, subst)
    elif occurs_check(var, x, subst):
        print(f"Occurs check failed: {var} occurs in {x}.")
        return None  # Avoid infinite loops in recursive substitutions
    else:
        print(f"Adding substitution: {var} -> {x}")
        new_subst = subst.copy()
        new_subst[var] = x
        return new_subst

def occurs_check(var, x, subst):
    """Check if var occurs in x to avoid infinite substitution."""
    if var == x:
        return True
    elif isinstance(x, tuple):
        return any(occurs_check(var, xi, subst) for xi in x)
    elif is_variable(x) and x in subst:
        return occurs_check(var, subst[x], subst)
    else:
        return False

def parse_sentence_to_expression(sentence):
    """Convert an English sentence to a logical expression."""
    sentence = sentence.strip().replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
    tokens = sentence.split()
    stack = []
    current = []

    for token in tokens:
        if token == "(":
            stack.append(current)
            current = []
        elif token == ")":
            if stack:
                last = stack.pop()
                last.append(tuple(current))
                current = last
        elif token == ",":
            continue
        else:
            current.append(token)

    return tuple(current) if len(current) == 1 else tuple(current)

def unification_with_explanation(expr1, expr2):
    """Perform unification on two expressions with step-by-step explanation."""
    print("\nStarting Unification Process...\n")
    subst = unify(expr1, expr2, {})
    if subst is not None:
        print("\nUnification Successful!")
        print("Substitution:", subst)
    else:
        print("\nUnification Failed!")

# Input from the user
print("Enter the logical expressions in English-like format.")
print("Example: Eats(x, Apple)")
sentence1 = input("Enter the first expression: ")
sentence2 = input("Enter the second expression: ")

# Parse sentences
expr1 = parse_sentence_to_expression(sentence1)
expr2 = parse_sentence_to_expression(sentence2)

# Perform unification with explanation
unification_with_explanation(expr1, expr2)