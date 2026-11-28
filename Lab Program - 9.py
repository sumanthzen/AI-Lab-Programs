
# First Order Logic Resolution

# Literal format: (negation, predicate, arguments)
# True means negated, False means positive

def substitute(term, subs):
    while term in subs:
        term = subs[term]
    return term


def apply_substitution(clause, subs):
    result = []
    for neg, pred, args in clause:
        new_args = tuple(substitute(a, subs) for a in args)
        result.append((neg, pred, new_args))
    return result


def resolve(c1, c2, i, j, subs):
    c1 = apply_substitution(c1, subs)
    c2 = apply_substitution(c2, subs)

    # Remove complementary literals
    result = c1[:i] + c1[i+1:] + c2[:j] + c2[j+1:]
    return result


def display(clause):
    if not clause:
        return "{}"

    parts = []
    for neg, pred, args in clause:
        name = pred + "(" + ",".join(args) + ")"
        parts.append(("~" if neg else "") + name)

    return " OR ".join(parts)


# Knowledge Base in CNF

C1 = [(True, "food", ("x",)),
      (False, "likes", ("John", "x"))]

C4 = [(True, "eats", ("x", "y")),
      (False, "killed", ("x",)),
      (False, "food", ("y",))]

C5 = [(False, "eats", ("Anil", "Peanuts"))]

C6 = [(False, "alive", ("Anil",))]

C9 = [(True, "alive", ("x",)),
      (True, "killed", ("x",))]

# Negated goal
C10 = [(True, "likes", ("John", "Peanuts"))]

print("FIRST ORDER LOGIC RESOLUTION")
print("--------------------------------")

# Step 1: Resolve C10 and C1
R1 = resolve(C10, C1, 0, 1, {"x": "Peanuts"})
print("Step 1:", display(R1))

# Step 2: Resolve C4 and C5
R2 = resolve(C4, C5, 0, 0,
             {"x": "Anil", "y": "Peanuts"})
print("Step 2:", display(R2))

# Step 3: Resolve C9 and C6
R3 = resolve(C9, C6, 0, 0, {"x": "Anil"})
print("Step 3:", display(R3))

# Step 4: Resolve R2 and R3
R4 = resolve(R2, R3, 0, 0, {})
print("Step 4:", display(R4))

# Step 5: Resolve R4 and R1
R5 = resolve(R4, R1, 0, 0, {})

print("Step 5:", display(R5))

if len(R5) == 0:
    print("\nEmpty clause obtained!")
    print("Hence, John likes Peanuts.")
    print("QUERY PROVED SUCCESSFULLY")
