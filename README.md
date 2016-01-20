# Smoothsteps

This repository holds a collection of [smootstep functions](https://en.wikipedia.org/wiki/Smoothstep) up to the 101st order equation. The 7th order equation was the last one published before these, by [Kyle McDonald](https://gist.github.com/kylemcdonald/77f916240756a8cfebef) back in 2015. This ones have been generated with the following technologies:

 * Pyhton2.7.
 * Sympy for solving the equation system.
 * NumPy for matrix operations.
 * Matplotlib for plotting (Even though the plotting starts to overflow at 35th order, the equations remain valid).

Disclaimer: Generator.py is the program that generates the program that calculates everything for a given order polynomial, this is bad design and should not be taken as a reference.

