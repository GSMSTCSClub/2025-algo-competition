# Summeria solving (Medium)

## Problem description
Gerald is playing a collaborative game called **Summaria** focused on reaching a target number `t` ($1 \leq t \leq 10^5$) with a certain set `S` of `n` ($1 \leq n \leq 10^5$) numbers. Help Gerald and his teammates win the game by determining a subset of `S` that has the sum of `t`.

## Input format
The first line of the standard input channel will contain `T` ($1 \leq T \leq 100$), the number of testcases. The first line of each test case contains `t` and `n`, with `t` being the target number and `n` being the length of `S`. The second line of each test case contains `n` space seperated positive integers representing the set of numbers in `S`. The numbers in `S` are unique.

## Output format
Print to the standard output channel the numbers of `S` that sum to `t` space seperated. The subset may be printed in any order and if there are multiple such subsets, then any may be printed. If no such subset exists, print `IMPOSSIBLE`.

## Sample 0
### Sample input:
```
3
10 3
1 9 5
5 8
1 2 3 4 5 6 7 8
6 4
99 65 45 21
```
### Sample output:
```
1 9
1 4
IMPOSSIBLE
```
### Explanation:
1. The only way to form `10` from `1 9 5` is `1 9`. Outputing `9 1` is also accepted.  
2. `5` can be formed from `1 2 3 4 5 6 7 8` in three ways as `1 4`, `2 3`, or `5`. Outputing any of these values is accepted.  
3. `6` cannot be formed from `99 65 45 21`.

### Constraints
$1 \leq T \leq 100$  
$1 \leq n, t \leq 10^5$  
$1 \leq S_i \leq 10^6$, where $S_i$ is the `i`th element of `S`.
