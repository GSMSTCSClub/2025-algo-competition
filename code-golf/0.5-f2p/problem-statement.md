# 0.5-f2p (easy)

## Problem description
As a "professional" (deeply addicted to the point of treating a game as a "job") free-to-play player of 8+ gacha (in-game luck-based loot boxes) games, you need an algorithm to handle the complexity of gambling and tell you if you have a higher than 50% chance to win a character (if so, you will spend your hard-earned game-currency on, don't ask me why you have this logic). You own $w$ wishes -- number of attempts to get a character. Each wish/attempt will have the rate depending on how many time you wished before. The algorithm should assume you have not wished anytime, and use the gacha's details to determine if you can win. Each game gacha's details is a dictionary of probabilities of obtaining a character in the current wish after x number of wishes.

Hint: The probabilities of each wish are independent (don't fail your middle school teacher)

## Input format
The first line is the number of test cases
Each test case, the first line is the number of wish you have
The second line is the number of entries "e" in the gacha's details dictionary 
Each line in the dictionary contains the $n$ number of wishes you must have done (not counting the current wish being done) and $r$ - the rate of winning (in percentage)  
The dictionary is sorted and guarantees an entry of 0 wishes done

## Sample 0
### Sample input:
```
2
60
3
0:0.1
40:0.2
90:100
60
2
0:1
40:2
```
### Sample output:
```
False
True
```

### Explanation:
The gacha base rate is 0.6% per wish

After 40 wishes, the 41st (1 indexing) to 80th wishes have the rate of 1.2% per wish

The character is guaranteed after 80 wishes

After hitting hard-pity more times than I can count, I assure you 60 wishes isn't sufficient for a 50% chance of winning


## Constraints
basic:
$0<=w<=1024$
$0<=e<=1024$
$0<=n<=1024$
$0<=r<=100$
## Output: 
True or False if the rate of winning the character given the number of wishes you have is higher than 50%

