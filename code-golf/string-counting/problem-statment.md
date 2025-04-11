# String Counting (Easy)

## Problem description
Gerald picked up a strange hobby from Bettsy the cow: substring counting. Bettsy, being the expert at this challenges Gerald to a match where the first animal to successfully count the number of a substring `S1` that can be found in `S2`. As such, they need a judging algorithm to help them settle debates. Please help Gerald and Bettsy by creating an algorithm that will determine the number of overlapping locations in `S2` of `S1`. (`S1` is guarenteed to be shorter than `S2`.)

## Input format
The first line contains `T`, the number of test cases in the test. The following `T` lines contain two space seperated strings of lowercase English characters. The first of these space seperated strings is `S1` and the second string is `S2`.

## Output format
For each test case, output the number of times that `S1` can be found in `S2`.

## Sample 0
### Sample input:
```
3
hello helloworldhello
testing testsarecool
aa aaaaaaaa
```
### Sample output:
```
2
0
7
```
### Explanation:
1. There are two instances of `hello` in **hello**`world`**hello**.  
2. There are zero instances of `testing` in `testsarecool`.
3. There are seven instances of `aa` in `aaaaaaaa`.

### Constraints
$1 \leq t \leq 100$  
$1 \leq$ `S1.len`$\leq$ `S2.len` $\leq 10^5$  
