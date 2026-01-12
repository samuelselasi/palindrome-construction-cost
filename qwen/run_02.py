import heapq
from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def can_form_palindrome(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    return odd_count <= 1

def solve(n, k, s):
    # First check if it's possible to form a palindrome
    if not can_form_palindrome(s):
        return -1
    
    # If already a palindrome and K=0, cost is 0
    if is_palindrome(s) and k == 0:
        return 0
    
    # Use Dijkstra-like approach with priority queue
    # State: (cost, string, remaining_swaps)
    pq = [(0, s, k)]
    # visited[state] = minimum cost to reach that state
    visited = {}
    
    while pq:
        cost, current_str, remaining_swaps = heapq.heappop(pq)
        
        # Skip if we've seen this state with lower cost
        state_key = (current_str, remaining_swaps)
        if state_key in visited and visited[state_key] < cost:
            continue
        
        # If we've used all swaps and have a palindrome
        if remaining_swaps == 0:
            if is_palindrome(current_str):
                return cost
            continue
        
        # Try all possible swaps
        for i in range(n):
            for j in range(i + 1, n):
                # Create new string by swapping characters at positions i and j
                new_str_list = list(current_str)
                new_str_list[i], new_str_list[j] = new_str_list[j], new_str_list[i]
                new_str = ''.join(new_str_list)
                
                # Calculate cost of this swap
                swap_cost = ord(current_str[i]) + ord(current_str[j])
                new_total_cost = cost + swap_cost
                
                # Check if we've seen this state before with lower cost
                new_state_key = (new_str, remaining_swaps - 1)
                
                if new_state_key not in visited or visited[new_state_key] > new_total_cost:
                    visited[new_state_key] = new_total_cost
                    heapq.heappush(pq, (new_total_cost, new_str, remaining_swaps - 1))
    
    return -1

# Read input
n, k = map(int, input().split())
s = input().strip()

result = solve(n, k, s)
print(result)
