
# Alpha-Beta Pruning Algorithm

def alpha_beta(node, alpha, beta, maximizing,
               path="Root"):

    # Check if node is a leaf
    if isinstance(node, int):
        print("Visited leaf:", node)
        return node

    if maximizing:
        value = float('-inf')

        for i, child in enumerate(node):
            value = max(value, alpha_beta(
                child, alpha, beta, False,
                path + " -> " + str(i + 1)
            ))

            alpha = max(alpha, value)

            # Pruning condition
            if alpha >= beta:
                print("Pruned at MAX node:", path)
                for remaining in node[i+1:]:
                    print("Pruned subtree:", remaining)
                break

        return value

    else:
        value = float('inf')

        for i, child in enumerate(node):
            value = min(value, alpha_beta(
                child, alpha, beta, True,
                path + " -> " + str(i + 1)
            ))

            beta = min(beta, value)

            # Pruning condition
            if beta <= alpha:
                print("Pruned at MIN node:", path)
                for remaining in node[i+1:]:
                    print("Pruned subtree:", remaining)
                break

        return value


# Given game tree
tree = [
    [[10, 9], [14, 18]],
    [[5, 4], [50, 3]]
]

print("ALPHA-BETA PRUNING")
print("-------------------")

result = alpha_beta(
    tree,
    float('-inf'),
    float('inf'),
    True
)

print("\nOptimal Root Value:", result)
print("Alpha-Beta Pruning Completed")
