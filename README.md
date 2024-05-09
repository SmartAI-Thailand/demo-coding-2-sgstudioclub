[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/cmUqWtY-)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15021405&assignment_repo_type=AssignmentRepo)
# Coding Challenge
## Challenge 1: Sum of Multiples
Problem Statement:
Write a function named sum_of_multiples that takes two integers: n and x. The function should return the sum of all multiples of x that are less than or equal to n.

**Examples:**

- If n = 20 and x = 5, the function should return 5 + 10 + 15 + 20 = 50.
- If n = 15 and x = 3, the function should return 3 + 6 + 9 + 12 + 15 = 45.

**Constraints:**

- 1 <= n <= 1000
- 1 <= x <= 100

### Function Signature:
```
def sum_of_multiples(n: int, x: int) -> int:
    pass
```

## Challenge 2: Minimum Window Substring
Problem Statement:
Write a function named min_window_substring that takes two strings: s and t. The function should return the minimal substring of s that contains all the characters in t. If no such substring exists, return an empty string.

**Examples:**

- If s = "ADOBECODEBANC" and t = "ABC", the minimal substring of s that contains all the characters in t is "BANC".
- If s = "a", and t = "aa", since s does not contain all the characters in t, return an empty string.

**Constraints:**
- The lengths of `s` and `t` are at most 10000.
- `s` and `t` consist of English letters.
### Function Signature:
```
def min_window_substring(s: str, t: str) -> str:
    pass
```
