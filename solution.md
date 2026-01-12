# Solution Explanation

## Algorithm Overview

This problem requires finding the minimum cost to reach a palindrome state using exactly K swaps. We use BFS (Breadth-First Search) with state memoization.

## Key Observations

1. **Small state space**: With n ≤ 10, there are at most 10! ≈ 3.6M possible string permutations, but palindrome constraints and K limit the reachable states significantly.

2. **State representation**: Each state is represented as (current_string, number_of_swaps_used). We need to track the minimum cost to reach each state.

3. **Palindrome checking**: A string is a palindrome if S[i] == S[n-1-i] for all i from 0 to n//2.

4. **Exact K swaps**: This is crucial - we can't stop early even if we reach a palindrome with fewer swaps. We must explore paths that use exactly K swaps.

## Algorithm Steps

### 1. State Representation
```
State = (string_as_tuple, swaps_used)
```

We use a tuple for the string to make it hashable for the dictionary.

### 2. BFS Approach

- Start with initial string at swap count 0
- For each state, generate all possible next states by trying all possible swaps
- Track minimum cost to reach each state
- Only update if we find a cheaper path to the same state
- Stop when we've processed all states with K swaps

### 3. Cost Calculation
For swapping positions i and j:

```
cost = ord(string[i]) + ord(string[j])
```

### 4. Answer Extraction
After BFS completes, check all states with exactly K swaps that are palindromes and return the minimum cost among them.

## Complexity Analysis

### Time Complexity
- **States**: O(n! × K) in worst case, but practically much smaller due to symmetry and palindrome constraints
- **Transitions per state**: O(n²) - trying all pairs of positions to swap
- **Overall**: O(n! × K × n²) worst case, but with n ≤ 10 and K ≤ 20, this is manageable

### Space Complexity
- O(n! × K) for storing states and their costs

## Why This Works

1. **Completeness**: BFS explores all possible sequences of K swaps systematically
2. **Optimality**: By tracking minimum cost to each state and processing in order, we ensure we find the cheapest path
3. **Correctness**: Only states with exactly K swaps that are palindromes are considered for the answer

## Edge Cases

1. **K = 0**: Check if the string is already a palindrome
2. **Impossible cases**: 
   - String with character counts that can't form a palindrome (more than one character with odd count for odd-length strings, any character with odd count for even-length strings)
   - K too small to reach any palindrome configuration
   - K has wrong parity (explained below)

## Parity Insight

An important observation: each swap changes the parity of inversions. If the minimum number of swaps needed to form any palindrome has a different parity than K, it's impossible (though with the ability to "waste" swaps by swapping and un-swapping, same parity is sufficient but not necessary in all cases - this makes the problem interesting).

However, with small K and the ability to swap any pair, we can often reach states with the right configuration by using extra swaps cleverly.

## Implementation Details

The solution uses:
- `collections.deque` for BFS queue
- Dictionary to track minimum cost to each state
- Tuple representation of strings for hashing
- Helper function to check palindrome property
