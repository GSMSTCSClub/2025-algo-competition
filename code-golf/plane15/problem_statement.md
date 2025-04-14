# Plane 15 (easy)

## Background
You're an undergrad at the Dream School. You know something is up if the experimental participation pays $100. The Dream Game is a horror game played in your dream. The dream may trap your conscience for up to 6 hours (like how you pull an all-nighter for that group project). If you are defeated, you will return to the start. You've made it to the last level-plane 15 and you just need to jump down the singularity to escape. 

## Problem description
You are spawned at location $(x,y)$ and Mafan the lonely Ghoul will spawn at $(a,b)$, the singularity is at $(0,0)$. You and Mafan have speed 1. Both will move in a continuous path with no obstacles. Both are simulated as points and collides when the locations are equal. You escape when you reach the singularity. If Mafan reaches you the instant you reach the singularity, you still escapes. This is because the game-engine loads your action first, even if you spawn at the same location with Mafan, within the first instance you can move infinitesimally away from Mafan. Similaraly, if you and Mafan both converge at the origin, your action is done right before Mafan's. If Mafan reaches you before then, you will not escape. Mafan will play optimally to prevent you from escaping. Output True or False whether you can escape. 

## Input format
The first line contains 2 space separated floats $x,y$
The second line contains 2 space separated floats $a,b$
## Output format

## Sample 0
### Sample input:
```
8 0
4 0
```
### Sample output:
```
False
```
### Explanation:
Mafan could just go to the origin and wait for you to come.

### Constraints
$0<x<=1024$
$0<y<=1024$
$0<a<=1024$
$0<b<=1024$