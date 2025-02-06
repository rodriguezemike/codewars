#https://www.codewars.com/kata/5416f1b54c24607e4c00069f/train/python

'''
Psuedocode (turtle and hare alg, floyd's algorthm)

function tortoise and hare(function f, value x0):
	let tortoise be f(x0) //Initalize tortoise at output of function at point x0
	let hare be f(f(x0)) //Initalize hare at output of tortoise
	let mu be 0 //Initalize mu as the index 0, mu here is the index of where the cycle begins
	let lambda be 1 //Initalize lambda as 1, lambda here is the length of the cycle lap or loop, must be at least 1 as we must visit some other place and return for it to be a cycle.

	//Tortoise and Hare will eventually meet up due to a cycle/lap/loop in our outputs/path.
	while tortoise and hare do not meet
		tortoise equals f(tortoise) //move tortoise 1 function output 
		hare equals f(f(hare)) // move hare 2 function outputs

	//After tortoise and hare meet up for the first time
	tortoise equals x0 //Move the tortoise back to the beginning
	//We let the hare run the lap/loop/cycle while the tortoise moves closer to the start
	//Eventually they will meet up at the beginning of the lap/cycle/loop
	while tortoise and hare do not meet
		tortoise equals f(tortoise) //move tortoise 1 function output closer to the start of the cycle
		hare equals f(hare) // move hare 1 function output along the cycle
		mu += 1 //1 step closer to the beginning(index) of our cycle/loop/lap
	//After second time they have met, we must find how long our lap/loop/cycle is
	//Our tortoise is at the start of the lap/loop/cycle in our path so we keep him at the start and move the hare one function output ahead of the tortoise and let the hare run the lap 1 function output (movement) at a time
	hare = f(tortoise)
	while toroise and hare do not meet
		hare = f(hare) //Move hare one function output (movement) at a time
		lambda += 1 // Incease the length of our lap/cycle/loop
'''

def floyd(f, x0):
    tortoise = f(x0)
    hare = f(tortoise)
    mu = 0
    lam = 1
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu +=1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
    return  [mu, lam]
