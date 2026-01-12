# Problem: Palindrome Construction Cost

## Problem Statement

You are given a string S of length n consisting of lowercase English letters, and an integer K.

You can perform a swap operation on the string: choose two positions i and j (1 ≤ i < j ≤ n) and swap the characters at these positions. The cost of this operation is value(S[i]) + value(S[j]), where value(c) is the ASCII value of character c (for lowercase letters: value('a') = 97, value('b') = 98, ..., value('z') = 122).

Your task is to determine the minimum total cost to transform S into a palindrome using exactly K swap operations. If it's impossible to make S a palindrome with exactly K swaps, output -1.

A string is a palindrome if it reads the same forwards and backwards.

## Input Format

The first line contains two integers n and K (1 ≤ n ≤ 10, 0 ≤ K ≤ 20) — the length of the string and the required number of swaps.

The second line contains a string S of length n consisting of lowercase English letters.

## Output Format

Output a single integer — the minimum total cost to make S a palindrome using exactly K swaps, or -1 if it's impossible.

## Examples

### Example 1
**Input:**
```
4 0
abba
```
**Output:**
```
0
```

**Explanation:**
The string is already a palindrome, and we need exactly 0 swaps. Cost is 0.

### Example 2
**Input:**
```
3 1
abc
```

**Output:**
```
-1
```

**Explanation:**
A string of odd length can be a palindrome, but "abc" has all different characters. Even after one swap, we cannot make it a palindrome. For example: swap(1,2)→"bac", swap(1,3)→"cba", swap(2,3)→"acb". None are palindromes.

### Example 3
**Input:**
```
4 1
abcd
```
**Output:**
```
-1
```
**Explanation:**
With all different characters in an even-length string, we cannot form a palindrome with just one swap.

### Example 4
**Input:**
```
6 2
aabbcc
```

**Output:**
```
392
```

**Explanation:**
We can rearrange to form a palindrome like "abccba" or "bacaab".
One optimal sequence: swap positions 2 and 5 (chars 'a' and 'c'): "aabbcc" → "acbbac" (cost = 97+99=196), then swap positions 3 and 4 (chars 'b' and 'b'): "acbbac" → "acbbac" (cost = 98+98=196). Total: 392.

### Example 5
**Input:**
```
5 3
aabaa
```

**Output:**
```
585
```

**Explanation:**
The string is already a palindrome "aabaa", but we need exactly 3 swaps. We must perform 3 swaps while maintaining or returning to a palindrome state.

### Example 6
**Input:**
```
2 1
ab
```

**Output:**
```
-1
```

**Explanation:**
After swapping the only two positions, we get "ba", which is not a palindrome (since 'b' ≠ 'a').

## Notes

- The string length is small (n ≤ 10), allowing for exploration of different states.
- K can be up to 20, so you may need to use more swaps than the minimum required to form a palindrome.
- If the string is already a palindrome but K > 0, you need to perform K swaps and still end with a palindrome.
