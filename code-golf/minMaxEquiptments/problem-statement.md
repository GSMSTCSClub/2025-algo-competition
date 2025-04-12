As a full-time gamer, you need to maximize your attack stat. You have a fixed number of enchanted equiptment slots, which equiptments should you select?

There are two main types:
>Add: give you an fixed increase in attack
>Mul: multiply your attack by some amount

The order you arraign them in your slots is the order in which your attack is modified. What is the max attack you can have (round down to nearest integer)? All slots don't have to be filled.

Input:
>The first line contains the number of test cases (c)

>For each test case

>>The first line contains, separated by space: int N (the number of slots), float I (your initial attack), int A (number of Add types), int M (number of Mul types)

>>The second line contains A floats separated by space of the Add type artifact's corresponding addition amount

>>The third line contains M floats separated by space of the Mul type artifact's corresponding multiplier

Output:

>for each test case, print an integer representing the rounded down (floor) maximum attack

Constraints:
>1 <= T < 8

>0 <= N < 64

>0 <= I < 64

>0 <= A < 64

>0 <= M < 8

>0 <= Add amount < 64

>1 <= Mul factor < 8
