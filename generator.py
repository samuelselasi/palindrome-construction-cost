#!/usr/bin/env python3
"""
Test case generator for Palindrome Construction Cost problem.
Generates random test cases with various properties.
"""

import random
import string

def generate_test_case(n, k, test_type="random"):
    """
    Generate a test case based on type.
    
    test_type options:
    - "random": completely random string
    - "palindrome": already a palindrome
    - "near_palindrome": one or two swaps away from palindrome
    - "impossible": cannot form palindrome
    """
    
    if test_type == "palindrome":
        # Generate a palindrome
        if n % 2 == 0:
            half = ''.join(random.choices(string.ascii_lowercase, k=n//2))
            s = half + half[::-1]
        else:
            half = ''.join(random.choices(string.ascii_lowercase, k=n//2))
            middle = random.choice(string.ascii_lowercase)
            s = half + middle + half[::-1]
    
    elif test_type == "near_palindrome":
        # Generate palindrome then mess it up slightly
        if n % 2 == 0:
            half = ''.join(random.choices(string.ascii_lowercase, k=n//2))
            s = list(half + half[::-1])
        else:
            half = ''.join(random.choices(string.ascii_lowercase, k=n//2))
            middle = random.choice(string.ascii_lowercase)
            s = list(half + middle + half[::-1])
        
        # Make 1-2 swaps to break palindrome property
        for _ in range(random.randint(1, 2)):
            i, j = random.sample(range(n), 2)
            s[i], s[j] = s[j], s[i]
        s = ''.join(s)
    
    elif test_type == "impossible":
        # For even length: use all different characters
        # For odd length: use characters with multiple odd counts
        if n % 2 == 0:
            s = ''.join(random.sample(string.ascii_lowercase, min(n, 26)))
        else:
            # Create string where too many characters have odd counts
            chars = random.sample(string.ascii_lowercase, min(n, 10))
            s = ''.join(chars[:n])
    
    else:  # random
        s = ''.join(random.choices(string.ascii_lowercase, k=n))
    
    return n, k, s

def main():
    """Generate several test cases."""
    
    test_configs = [
        (4, 0, "palindrome"),      # Already palindrome, k=0
        (3, 1, "impossible"),       # Impossible case
        (4, 1, "random"),           # Small random
        (6, 2, "near_palindrome"),  # Near palindrome
        (5, 3, "random"),           # Odd length
        (2, 1, "impossible"),       # Minimal impossible
        (8, 4, "random"),           # Larger case
        (10, 5, "near_palindrome"), # Max size
    ]
    
    for i, (n, k, test_type) in enumerate(test_configs, 1):
        n, k, s = generate_test_case(n, k, test_type)
        
        print(f"=== Test Case {i} ===")
        print(f"Type: {test_type}")
        print(f"Input:")
        print(f"{n} {k}")
        print(f"{s}")
        print()

if __name__ == "__main__":
    main()
