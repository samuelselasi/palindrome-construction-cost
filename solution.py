from collections import deque

def is_palindrome(s):
    """Check if a string is a palindrome"""
    return s == s[::-1]

def solve():
    n, k = map(int, input().split())
    s = input().strip()
    
    # Edge case: if k=0, check if already palindrome
    if k == 0:
        print(0 if is_palindrome(s) else -1)
        return
    
    # BFS to explore all states
    # State: (string_as_tuple, swaps_used)
    # Value: minimum_cost to reach this state
    
    initial_state = (tuple(s), 0)
    queue = deque([initial_state])
    
    # min_cost[(string_tuple, swaps)] = minimum cost to reach this state
    min_cost = {initial_state: 0}
    
    while queue:
        current_str, swaps = queue.popleft()
        current_cost = min_cost[(current_str, swaps)]
        
        # If we've used k swaps, don't generate more states
        if swaps == k:
            continue
        
        # Try all possible swaps
        str_list = list(current_str)
        for i in range(n):
            for j in range(i + 1, n):
                # Swap positions i and j
                str_list[i], str_list[j] = str_list[j], str_list[i]
                new_str = tuple(str_list)
                new_swaps = swaps + 1
                swap_cost = ord(current_str[i]) + ord(current_str[j])
                new_cost = current_cost + swap_cost
                
                new_state = (new_str, new_swaps)
                
                # Update if we found a cheaper path to this state
                if new_state not in min_cost or new_cost < min_cost[new_state]:
                    min_cost[new_state] = new_cost
                    queue.append(new_state)
                
                # Swap back for next iteration
                str_list[i], str_list[j] = str_list[j], str_list[i]
    
    # Find minimum cost among all states with exactly k swaps that are palindromes
    answer = float('inf')
    for (str_tuple, swaps), cost in min_cost.items():
        if swaps == k and is_palindrome(''.join(str_tuple)):
            answer = min(answer, cost)
    
    print(answer if answer != float('inf') else -1)

if __name__ == "__main__":
    solve()
