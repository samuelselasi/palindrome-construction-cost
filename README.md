# Palindrome Construction Cost - Competitive Programming Problem

## Overview
This is an original Div1/Div2 level competitive programming problem that combines string manipulation, graph-based state exploration, and optimization under constraints.

## Problem Summary
Given a string and an integer K, find the minimum cost to transform the string into a palindrome using exactly K swap operations, where each swap costs the sum of ASCII values of the swapped characters.

## Difficulty Level
**Codeforces Div1/Div2** - Requires understanding of:
- BFS/state space exploration
- Dynamic programming concepts
- Palindrome properties
- Optimization under constraints

## Quick Start

### Testing the Solution
```bash
python solution.py < test_cases/1.in
```

### Expected Output
```
0
```

### Running All Tests
```bash
for i in {1..6}; do
  echo "Test $i:"
  python solution.py < test_cases/$i.in
  echo "Expected: $(cat test_cases/$i.out)"
  echo
done
```

## File Structure
- `problem.md` - Full problem statement
- `solution.md` - Algorithm explanation
- `solution.py` - Optimal solution (BFS-based)
- `idea.md` - Problem development process
- `test_cases/` - 6 comprehensive test cases
- `qwen/` - Failed attempts from Qwen model
- `requirements.json` - Time/memory limits

## Key Insights
1. Small constraints (n ≤ 10, K ≤ 20) allow state exploration
2. Exact K constraint makes greedy approaches fail
3. BFS with state memoization ensures optimality
4. Palindrome constraint significantly prunes search space

## Originality
This problem is original and combines multiple concepts in a novel way:
- Character-value dependent swap costs (not position-dependent)
- Exact operation count requirement (not minimum)
- Multiple optimization dimensions (cost, swaps, palindrome)

The problem has been verified to not match existing problems through search engine checks.

## Testing Notes
- Test cases cover: already palindrome, impossible cases, small strings, larger strings
- Edge cases include K=0, odd/even length strings, various character distributions
- Solution is verified to pass all test cases within time limits

## LLM Benchmark Results
I tested the problem against the Qwen-2.5-Coder-32B model (and variants) to verify difficulty. The model consistently failed to find the optimal path, often falling into "greedy" traps where it selected the first valid path rather than the cheapest one.

Script: `python3 test_runner.py`

TEST CASE                 | SOLUTION   | RUN_01     | RUN_02     | RUN_03     
-------------------------------------------------------------------------------------
1. Classic Trap (aba)     | 388        | 390 * | 388        | 390 * 2. High Val Mid (aza)     | 388        | 438 * | 388        | 438 * 3. Descending (cba)       | -1         | -1         | -1         | -1         
4. High Val Seq (zyx)     | -1         | -1         | -1         | -1         
5. Even Mirror (abba)     | 388        | 390 * | 388        | 390 * 6. Long Mirror (abcba)    | 388        | 390 * | 388        | 390 * -------------------------------------------------------------------------------------
* Denotes a failure (result differs from solution.py)

### Failure Analysis:

- **Run 01 & 03**: Failed due to unweighted BFS logic. The models prioritized finding any solution with K swaps rather than the minimum cost solution, consistently overpaying on simple palindromes like `aba` (Cost 390 vs Optimal 388).
