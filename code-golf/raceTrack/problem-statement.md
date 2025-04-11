You are the developer of a simple game where a car goes down a track, the player can move the car left or right.

To spice things up, players can create and publish their own racetrack, however, you must determine if the racetrack is valid.

The race track is valid if it contains a complete road (not obstructed by obstacles) that can be travelled by goind down, left, or right one at a time.

Input:
>The first line contains the number of test cases (c)

>Each test case contains:

>>w,l (width and length of the race track separated by comma)

>>l lines with each line containing w:

>>>w characters of the obstacle (1) or road square (0).

Output:

>for each test case, print True or False if the player can travel from the starting anywhere from the top row to the bottom row.