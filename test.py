from itertools import combinations, permutations, combinations_with_replacement, permutations_with_replacement

# 조합 (Combinations)
arr = ['A', 'B', 'C']
comb = list(combinations(arr, 2))
print("조합:", comb)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 순열 (Permutations)
perm = list(permutations(arr, 2))
print("순열:", perm)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 다중 조합 (Combinations with replacement)
comb_rep = list(combinations_with_replacement(arr, 2))
print("다중 조합:", comb_rep)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 다중 순열 (Permutations with replacement)
perm_rep = list(permutations_with_replacement(arr, 2))
print("다중 순열:", perm_rep)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
