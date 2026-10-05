# Project 3: Haunted House

Completed for CS 4150 Algorithms with Travis Martin (FA26).

# Assignment Description

Prog3 - Haunted House

Fall 2026
Home
Piazza
Assignments
Gradescope
Poll Everywhere
Syllabus
Grades1
Notebook
Prog3 - Haunted House
Due: Tue Oct 6, 2026 11:59pm
50 Points Possible
Attempt 1
In Progress
NEXT UP: Submit Assignment

Your solution to this problem must be an iterative dynamic programming algorithm. It cannot be a memoized recursive algorithm.

Due date is delayed by 1 week because of the midterm -- prioritize the midterm, but completing this wouldn't hurt for the midterm (DP will be on the midterm, but it won't be a large focus).

Please see Tips for programming problems for more instructions on solving programming problems.

 

A long haunted house has 2𝑁 rooms. The house is laid out as 𝑁 rows of 2 rooms side-by-side. Doors connect all adjacent rooms (north-south and east-west, but not diagonally). You, the scare master of the haunted house, unfortunately must close off 𝑘 of the rooms because of staffing cuts. Visitors must be able to enter using at least one of the two rooms at one end of the house, proceed through the house, and exit from at least one of the two rooms at the other end.

Therefore, you may not close off any two rooms that would block passage through the haunted house. That is, you may not block off two rooms in the same row or two rooms in adjacent rows that touch diagonally. Furthermore, you've determined the scare factor of each room, and so you want to close off those 𝑘 rooms that leave the most scariness remaining, without blocking passage through the house.

\includegraphics[width=.7in]{fig}
Figure 1: This haunted house shows an optimal solution to the third sample input problem. The gray rooms show those that should be closed.
Input
Each problem instance will begin with a line containing two integers 𝑁 and 𝑘, where 3≤𝑁≤200 gives the number of rows, and 0≤𝑘≤𝑁 gives the number of rooms that must be closed off. This is followed by 𝑁 rows of two integers, giving the scare factors of the two rooms in that row. Each room’s value f satisfies 0≤f≤100.

Output
For each house, output the total scariness remaining in the entire house, after closing k optimal rooms. Your algorithm must finish in less than 1 second per test case.

Sample Input 1	Sample Output 1
6 4
3 1
2 1
1 2
1 3
3 3
0 0
17
 

Sample Input 2	Sample Output 2
4 3
3 4
1 1
1 1
5 6
17
 

Sample Input 3	Sample Output 3
10 5
7 8
4 9
3 7
5 9
7 2
10 3
0 10
3 2
6 3
7 9
102
Sample input 4Download Sample input 4, Sample answer 4
