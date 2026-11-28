
# Unification in First Order Logic

# Check whether a term is a variable
def is_variable(x):
    return isinstance(x, str) and x.startswith('?')


# Apply existing substitutions
def apply_subst(term, subst):
    if is_variable(term) and term in subst:
        return apply_subst(subst[term], subst)

    if isinstance(term, tuple):
        return tuple(apply_subst(x, subst) for x in term)

    return term


# Occurs check
def occurs(var, term, subst):
    term = apply_subst(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, x, subst) for x in term)

    return False


# Unification algorithm
def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = apply_subst(x, subst)
    y = apply_subst(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        if occurs(x, y, subst):
            return None
        subst[x] = y
        return subst

    if is_variable(y):
        if occurs(y, x, subst):
            return None
        subst[y] = x
        return subst

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    return None


# Main program
E1 = ('Eats', '?x', 'Apple')
E2 = ('Eats', 'Riya', '?y')

result = unify(E1, E2)

if result is not None:
    print("Unification Successful!")
    print("Substitution:", result)
    print("Expression 1:", apply_subst(E1, result))
    print("Expression 2:", apply_subst(E2, result))
else:
    print("Unification Failed!")
