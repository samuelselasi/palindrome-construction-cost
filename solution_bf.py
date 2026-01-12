#!/usr/bin/env python3
"""
Brute force solution for Palindrome Construction Cost.
Uses recursive backtracking to explore all possible sequences of K swaps.
This is slower but useful for verification on small inputs.
"""

def is_palindrome(s):
    """Check if a string is a palindrome"""
    return s == s[::-1]

def solve_recursive(s, k, swaps_done, current_cost):
    """
    Recursively try all possible swap sequences.
    Returns minimum cost to reach palindrome with exactly k swaps.
    """
    n = len(s)
    
    # Base case: used exactly k swaps
    if swaps_done == k:
        if is_palindrome(s):
            return current_cost
        return float('inf')
    
    # Try all possible swaps
    min_cost = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            # Swap positions i and j
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            new_s = ''.join(s_list)
            
            # Calculate swap cost
            swap_cost = ord(s[i]) + ord(s[j])
            
            # Recursively solve for remaining swaps
            result = solve_recursive(new_s, k, swaps_done + 1, current_cost + swap_cost)
            min_cost = min(min_cost, result)
    
    return min_cost

def solve():
    """Main solve function"""
    n, k = map(int, input().split())
    s = input().strip()
    
    # Edge case: if k=0, check if already palindrome
    if k == 0:
        print(0 if is_palindrome(s) else -1)
        return
    
    # Use recursive brute force
    result = solve_recursive(s, k, 0, 0)
    
    print(result if result != float('inf') else -1)

if __name__ == "__main__":
    solve()

# Note: This solution has exponential time complexity O((n^2)^k)
# It's only practical for very small inputs but guarantees correctness
# Useful for verifying test cases against the optimized BFS solution
