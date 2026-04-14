"""
Finite Topology Enumeration via One-Point Expansion

Reference implementation accompanying the paper:
"Enumerating Finite Topologies via One-Point Expansions of Preorder Digraphs"

This script:
- Computes N(G) for a given preorder digraph
- Generates all labeled preorder digraphs (small n)
- Verifies T(n+1) = sum N(G)

NOTE:
This implementation prioritizes clarity and correctness.
For large-scale computations, bitmask representations are recommended.
"""

import itertools


def compute_extension_number(n, edges):
    """
    Computes the extension number N(G) for a preorder digraph G.

    Parameters:
        n (int): number of vertices
        edges (list of tuples): reflexive + transitive relation

    Returns:
        int: N(G)
    """
    vertices = list(range(1, n + 1))

    # Build reachability sets R(u)
    reachability = {u: set() for u in vertices}
    for u, v in edges:
        reachability[u].add(v)

    # Generate all subsets
    all_subsets = []
    for r in range(n + 1):
        all_subsets.extend(itertools.combinations(vertices, r))
    all_subsets = [set(s) for s in all_subsets]

    # Down-sets
    down_sets = []
    for s in all_subsets:
        is_down = True
        for x in s:
            for u in vertices:
                if x in reachability[u] and u not in s:
                    is_down = False
                    break
            if not is_down:
                break
        if is_down:
            down_sets.append(s)

    # Up-sets
    up_sets = []
    for s in all_subsets:
        is_up = True
        for x in s:
            for v in reachability[x]:
                if v not in s:
                    is_up = False
                    break
            if not is_up:
                break
        if is_up:
            up_sets.append(s)

    # Count admissible pairs
    N = 0
    for A in down_sets:
        if not A:
            common = set(vertices)
        else:
            common = set.intersection(*(reachability[a] for a in A))

        for B in up_sets:
            if B.issubset(common):
                N += 1

    return N


def generate_all_preorders(n):
    """
    Generates all labeled preorder digraphs on n vertices.

    WARNING: exponential — usable only for small n.
    """
    vertices = list(range(1, n + 1))
    possible_edges = list(itertools.product(vertices, vertices))

    mandatory = [(i, i) for i in vertices]
    other_edges = [e for e in possible_edges if e[0] != e[1]]

    valid = []

    for r in range(len(other_edges) + 1):
        for combo in itertools.combinations(other_edges, r):
            edges = mandatory + list(combo)

            # check transitivity
            adj = {u: set() for u in vertices}
            for u, v in edges:
                adj[u].add(v)

            ok = True
            for i in vertices:
                for j in adj[i]:
                    for k in adj[j]:
                        if k not in adj[i]:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break

            if ok:
                valid.append(edges)

    return valid


def main():
    print("=== Finite Topology Enumeration ===")

    # Example 1: Chain n=3
    chain_3 = [(1,1),(2,2),(3,3),(2,1),(3,2),(3,1)]
    print("N(G) for chain (n=3):", compute_extension_number(3, chain_3))

    # Example 2: Non-chain n=4
    non_chain_4 = [(1,1),(2,2),(3,3),(4,4),(3,1),(3,2),(4,1),(4,2)]
    print("N(G) for non-chain (n=4):", compute_extension_number(4, non_chain_4))

    # Compute T(n)
    results = {1: 1}

    for n in range(1, 5):  # keep safe
        preorders = generate_all_preorders(n)
        total = sum(compute_extension_number(n, G) for G in preorders)
        results[n+1] = total
        print(f"T({n+1}) = {total}")

    print("Results:", results)


if __name__ == "__main__":
    main()
