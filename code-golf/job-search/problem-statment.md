# Gerald's Job Search (Medium)

## Problem description
Gerald, the aspiring daredevil hamster has unfortunately been recently let go of his previous job position as a hoop jumper. The hamster job market is poor right now, with $j$ open positions ($2 ≤ j ≤ 10$) with $n$ key skill requirements ($1 ≤ n ≤ 10$) of a length $l$ characters ($5 ≤ l ≤ 150,000$). Gerald is most fit for the position in which his $s$ skills ($1 ≤ s ≤ 10$) with $l$ characters overlap most with the skill requirements in the job positions. Please help Gerald by creating an algorithm to sort the job positions by how well Gerald fits with the job positions, breaking ties by sorting the names of the job positions.

## Input format
The first line of each file will contain $j$, $n$, $l$, and $s$ separated by spaces. The first $s$ lines will contain Gerld's skills. The following $j * (n + 1)$ lines will contain the open job postings. The first line for each job posting is the name of the posting, and the following $n$ lines are the skills requirements of the postings.

## Output format
Print to the standard output channel the names of the companies sorted in descending order of how many characters of Gerld's skillset match the descriptions provided by the companies, and break ties by sorting the names of the job positions in lexicographically increasing order.

## Sample 0
### Sample input:
```
2 2 6 2
Python
kotlin
Fangoogle
Sealin
Pyxotl
Bookface
Dokotl
Pygame
```
### Sample output:
```
Bookface Fangoogle
```
### Explanation:
Sea**lin** overlaps with kot**lin** in three places, and Pyx**otl** overlaps with k**otl**in in three places, meaning there is a total overlap of 6 characters for `Fangoogle`. Do**kotl** and **kotl**in overlap in four places, and **Py**game overlaps with **Py**thon in two places, meaning there is a total overlap of 6 characters for `Bookface`. There is a tie in matched characters so we use lexicographical order to sort these companies. `Bookface` is lexicographically less than `Fangoogle`, thus the output is `Bookface Fangoogle`.


### Constraints
$2 ≤ j ≤ 10$  
$1 ≤ n ≤ 10$  
$5 ≤ l ≤ 150,000$  
$1 ≤ s ≤ 10$  
$jnls < 300,000$  
`Job position names are unique and are less than or equal to 30 characters.`  
`All skills described in the job positions are upper and lower case English characters.`  
`Test cases 0-8 have l ≤ 500. Test cases 9-15 have no additional constraints for l.`