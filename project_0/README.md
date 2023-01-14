# Project 0. Guess the number game


### Description

This code contains two functions, random_number and guess.

random_number is a simple function that generates a random integer between 1 and 100, inclusive, and returns it.

guess is a function that takes an integer as an argument and tries to guess the number in as few attempts as possible. It uses a binary search algorithm to accomplish this. The function starts by initializing a count variable to keep track of the number of guesses it takes, and a current variable that is set to 50. The function also initializes a step variable to 50.

The function then enters a while loop and each iteration, the step value is divided by 2 and rounded up to ensure that it does not become 0. The count variable is then incremented by 1. If the current variable is equal to the number passed to the function, the count variable is returned. If the number passed to the function is greater than the current variable, the current variable is incremented by the step value. If the number passed to the function is less than the current variable, the current variable is decremented by the step value.

The guess function returns the number of guesses it took to find the number.

### Quality Metric

The results are evaluated by the average number of attempts at 1000 repetitions. It is necessary to achieve a minimum number of attempts.

### What I practice

* Learn how to write good Python code.
* Learning to work with IDE.
* Learning to work with GitHub.

### Result

My function guesses the number on average in 5.9 attempts.

It also makes no more than 7 attempts.


I enjoyed making a proper python project.

Clean and simple code, coments and PEP8 complient style.

Hope I did a good job.
