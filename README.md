# Week 3 Assignment on Conditions and Loops

- `grade_reporter.py`: Loops through a list of scores, gives each one a grade, and prints how many passed, how many failed, and the average.
- `bug_hunt.py`: A broken program that I fixed so it correctly prints the sum of 1 to 5.

The hardest bug to find was the `count < 5` condition in the while loop. There was no error message, but the program printed 10 when I expected 15. I added the numbers 1 to 5 in my head, saw that the answer should be 15, and realised the loop was stopping before it added 5, so I changed it to `count <= 5`.
