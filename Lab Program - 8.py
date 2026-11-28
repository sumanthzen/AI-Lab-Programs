
# First Order Logic using Forward Chaining

# Initial Knowledge Base (Facts)
KB = [
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
]

# Variables used in the rules
variables = {"x", "y", "z"}

# Rules: (Premises, Conclusion)
rules = [
    # Missiles are weapons
    ([("Missile", "x")],
     ("Weapon", "x")),

    # Missiles owned by A were sold by Robert to A
    ([("Missile", "x"), ("Owns", "A", "x")],
     ("Sells", "Robert", "x", "A")),

    # Enemy of America is hostile
    ([("Enemy", "x", "America")],
     ("Hostile", "x")),

    # An American selling weapons to hostile nations is criminal
    ([("American", "x"),
      ("Weapon", "y"),
      ("Sells", "x", "y", "z"),
      ("Hostile", "z")],
     ("Criminal", "x"))
]


# Function to match facts with rule conditions
def unify(pattern, fact, theta):
    theta = theta.copy()

    if pattern[0] != fact[0]:
        return None

    for p, f in zip(pattern[1:], fact[1:]):
        if p in variables:
            if p in theta:
                if theta[p] != f:
                    return None
            else:
                theta[p] = f
        elif p != f:
            return None

    return theta


# Function for matching all conditions of a rule
def match_conditions(conditions, facts, theta=None):
    if theta is None:
        theta = {}

    if not conditions:
        yield theta
        return

    first = conditions[0]

    for fact in facts:
        new_theta = unify(first, fact, theta)

        if new_theta is not None:
            yield from match_conditions(
                conditions[1:], facts, new_theta
            )


# Apply substitution to the conclusion
def substitute(conclusion, theta):
    return tuple(theta.get(x, x) for x in conclusion)


# Forward Chaining Algorithm
def forward_chaining(KB, rules, query):

    print("Initial Knowledge Base:")
    for fact in KB:
        print(fact)

    print("\nForward Chaining Process:")

    if query in KB:
        print("Query already exists in KB.")
        return True

    while True:
        new_facts = []

        for premises, conclusion in rules:

            for theta in match_conditions(premises, KB):

                result = substitute(conclusion, theta)

                if result not in KB and result not in new_facts:

                    new_facts.append(result)
                    print("Inferred:", result)

                    if result == query:
                        print("\nQuery Proved Successfully!")
                        return True

        if not new_facts:
            break

        KB.extend(new_facts)

    print("\nQuery Cannot Be Proved!")
    return False


# Given Query
query = ("Criminal", "Robert")

# Execute Forward Chaining
forward_chaining(KB, rules, query)
