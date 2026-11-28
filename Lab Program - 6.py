
# Truth Table Enumeration for Propositional Logic

# Knowledge Base
def KB(model):
    P = model['P']
    Q = model['Q']
    R = model['R']

    return ((not Q or P) and
            (not P or not Q) and
            (Q or R))


# Query evaluation
def query(model, choice):
    P = model['P']
    Q = model['Q']
    R = model['R']

    if choice == 1:
        return R
    elif choice == 2:
        return not R or P
    elif choice == 3:
        return not Q or R


# Truth table enumeration algorithm
def TT_CHECK_ALL(symbols, model, choice):

    if len(symbols) == 0:
        if KB(model):
            return query(model, choice)
        return True

    P = symbols[0]
    rest = symbols[1:]

    return (TT_CHECK_ALL(rest, {**model, P: True}, choice)
            and
            TT_CHECK_ALL(rest, {**model, P: False}, choice))


# Main function
symbols = ['P', 'Q', 'R']

for i in range(1, 4):
    result = TT_CHECK_ALL(symbols, {}, i)

    if i == 1:
        print("KB entails R:", result)
    elif i == 2:
        print("KB entails R -> P:", result)
    else:
        print("KB entails Q -> R:", result)
