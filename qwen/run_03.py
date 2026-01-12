from collections import deque
import sys

def is_palindrome(s):
    return s == s[::-1]

def can_form_palindrome(s):
    # Count frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    
    # Count characters with odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    
    # For palindrome: at most one character can have odd frequency
    return odd_count <= 1

def solve(n, k, s):
    # Check if it's possible to form a palindrome at all
    if not can_form_palindrome(s):
        return -1
    
    # If already a palindrome and K=0, cost is 0
    if is_palindrome(s) and k == 0:
        return 0
    
    # Use BFS to find minimum cost
    # State: (string, swaps_used, cost)
    queue = deque([(s, 0, 0)])
    visited = set()
    visited.add((s, 0))
    
    min_cost = float('inf')
    
    while queue:
        current_s, swaps_used, cost = queue.popleft()
        
        # If we've used exactly K swaps and have a palindrome
        if swaps_used == k and is_palindrome(current_s):
            min_cost = min(min_cost, cost)
            continue
        
        # If we've used K swaps but not a palindrome, skip
        if swaps_used == k:
            continue
            
        # Try all possible swaps
        for i in range(n):
            for j in range(i + 1, n):
                # Create new string by swapping characters at positions i and j
                new_s_list = list(current_s)
                new_s_list[i], new_s_list[j] = new_s_list[j], new_s_list[i]
                new_s = ''.join(new_s_list)
                
                # Calculate cost of this swap
                swap_cost = ord(current_s[i]) + ord(current_s[j])
                new_cost = cost + swap_cost
                new_swaps = swaps_used + 1
                
                # Only continue if we haven't exceeded K swaps
                if new_swaps <= k:
                    state = (new_s, new_swaps)
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_s, new_swaps, new_cost))
    
    return min_cost if min_cost != float('inf') else -1

# Read input
n, k = map(int, input().split())
s = input().strip()

result = solve(n, k, s)
print(result)
