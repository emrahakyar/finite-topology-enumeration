# Finite Topology Enumeration via One-Point Expansion

This repository contains a reference Python implementation accompanying the paper:

**"Enumerating Finite Topologies via One-Point Expansions of Preorder Digraphs"**

## Overview

This code implements:

- Computation of the extension number \(N(G)\)
- Enumeration of labeled preorder digraphs (for small \(n\))
- Verification of the recursive formula:

\[
T(n+1) = \sum_{G \in \mathcal{P}_n} N(G)
\]

## Features

- Direct implementation of the paper’s definitions
- Verification of worked examples
- Experimental computation of \(T(n)\) for small \(n\)

## Usage

Run:

```bash
python finite_topology_enumeration.py
