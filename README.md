# Associated Paper

This repository accompanies the paper:

**Enumerating Finite Topologies via One-Point Expansions of Preorder Digraphs**

**Authors:** Emrah Akyar, Handan Akyar

*(under submission)*

# Finite Topology Enumeration via One-Point Expansion

This repository contains a reference Python implementation accompanying the paper:

**"Enumerating Finite Topologies via One-Point Expansions of Preorder Digraphs"**

## Overview

This code implements:

- Computation of the extension number $N(G)$
- Enumeration of labeled preorder digraphs (for small $n$)
- Verification of the recursive formula:

$$
T(n+1) = \sum_{G \in \mathcal{P}_n} N(G)
$$

## Features

- Direct implementation of the paper’s definitions
- Verification of worked examples
- Experimental computation of $T(n)$ for small $n$

## Usage

Run:

```bash
python finite_topology_enumeration.py
```

## Notes

- This implementation prioritizes clarity over performance.
- The algorithm is exponential and suitable only for small $n$.
- For larger computations, bitmask-based implementations are recommended.

## Example Output

```text
N(G) for chain (n=3): 13
N(G) for non-chain (n=4): 26
T(2) = 4
T(3) = 29
T(4) = 355
T(5) = 6942
```

## License

This project is licensed under the MIT License.

## Citation

If you use this code, please cite:

Akyar, E., Akyar, H.  
*Enumerating Finite Topologies via One-Point Expansions of Preorder Digraphs*, 2026.
