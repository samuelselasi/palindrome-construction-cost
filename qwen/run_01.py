from collections import deque
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def can_form_palindrome(s):
    # Count frequency of each character
    freq = Counter(s)
    # Count how many characters have odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    # For palindrome: at most one character can have odd frequency
    return odd_count <= 1

def solve(n, k, s):
    # First check if it's possible to form a palindrome at all
    if not can_form_palindrome(s):
        return -1
    
    # If already a palindrome and K=0, cost is 0
    if is_palindrome(s) and k == 0:
        return 0
    
    # Use BFS to find minimum cost to reach palindrome with exactly K swaps
    # State: (current_string, swaps_used, cost)
    queue = deque([(s, 0, 0)])
    visited = set()
    visited.add((s, 0))
    
    min_cost = float('inf')
    
    while queue:
        current_str, swaps_used, current_cost = queue.popleft()
        
        # If we've used exactly K swaps and current string is palindrome
        if swaps_used == k and is_palindrome(current_str):
            min_cost = min(min_cost, current_cost)
            continue
        
        # If we've used K swaps but not palindrome, skip
        if swaps_used >= k:
            continue
        
        # Try all possible swaps
        for i in range(n):
            for j in range(i + 1, n):
                # Create new string by swapping positions i and j
                new_str = list(current_str)
                new_str[i], new_str[j] = new_str[j], new_str[i]
                new_str = ''.join(new_str)
                
                # Calculate cost of this swap
                swap_cost = ord(current_str[i]) + ord(current_str[j])
                new_swaps = swaps_used + 1
                new_cost = current_cost + swap_cost
                
                # Check if we've seen this state before
                state = (new_str, new_swaps)
                if state not in visited:
                    visited.add(state)
                    queue.append((new_str, new_swaps, new_cost))
    
    return min_cost if min_cost != float('inf') else -1

# Read input
n, k = map(int, input().split())
s = input().strip()

# Solve and output
result = solve(n, k, s)
print(result)
