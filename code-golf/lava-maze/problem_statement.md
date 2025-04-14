# Lava maze (Hard)

## Problem description
Gerald is trying to design a challenging maze for his "friends" to escape. Unfortunately, Gerald cannot find any contracters that are willing to build the maze, especially with the lava that he wants to use, but he has recieved a shipment of dirt perfectly stacked in columns of 1 turkey vulture by 1 turkey vulture on a `n` by `n` grid. Gerald has walls surrounding the dirt columns and has an infinite amount of lava that he can distribute as he pleases to a level `l` with the press of a magic button. Gerald wants to find the highest level that he can set the lava such that it is possible to reach the bottom right of the maze from the top left just by moving to adjacent pillers of dirt extending above the height of the lava. Please help Gerald build this crazy maze by finding the greatest value of `l` such that it is possible to complete the maze.

## Input format
The first line contains `n` the size of the grid. The following `n` lines contain `n` space seperated positive integers.

## Output format
Print to the standard output channel the greatest level `l` such that it is possible to reach the bottom left of the maze from the top left of the maze.

## Sample 0
### Sample input:
```
10
9 5 3 2 4 6 8 4 2 5
8 7 6 4 1 5 2 4 8 4
6 3 8 9 4 2 1 5 8 4
8 6 2 4 7 9 9 3 2 1
4 5 9 5 6 7 8 2 1 3
1 2 3 2 5 4 8 5 4 8
4 6 3 2 7 8 5 4 9 1
1 5 7 6 3 4 8 2 5 9
5 6 3 4 2 1 8 2 7 6
4 5 6 4 2 3 7 9 5 9
```
### Sample output:
```
5
```
### Explanation:
When the lava level is set to 5, the grid looks like the following (1 means that a position is above the lava and 0 means it is submerged by the lava):
```
1 1 0 0 0 1 1 0 0 1
1 1 1 0 0 1 0 0 1 0
1 0 1 1 0 0 0 1 1 0
1 1 0 0 1 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0
0 0 0 0 1 0 1 1 0 1
0 1 0 0 1 1 1 0 1 0
0 1 1 1 0 0 1 0 1 1
1 1 0 0 0 0 1 0 1 1
0 1 1 0 0 0 1 1 1 1
```
There is a path from the topleft to the bottom right.  
When the lava level is set to 6, the grid looks like the following (1 means that a position is above the lava and 0 means it is submerged):
```
1 0 0 0 0 1 1 0 0 0
1 1 1 0 0 0 0 0 1 0
1 0 1 1 0 0 0 0 1 0
1 1 0 0 1 1 1 0 0 0
0 0 1 0 1 1 1 0 0 0
0 0 0 0 0 0 1 0 0 1
0 1 0 0 1 1 0 0 1 0
0 0 1 1 0 0 1 0 0 1
0 1 0 0 0 0 1 0 1 1
0 0 1 0 0 0 1 1 0 1
```
There is no path from the top left to the bottom right; therefore, the greatest value for `l` such that the maze is completable is 5.

### Constraints
$1 \leq n \leq 1,000$  
$1 \leq n_{ij} \leq 10^9$  
