Matthew Svenson 2023

What is this software?

    This software simulates the collision of two blocks in addition to a wall with infinite mass and zero velocity with user inputted
    mass as well as user inputted velocity for the two blocks. This project was made to simulate the strange coincidence of pi showing
    up in block collisions when the first block is static with a mass of 1kg and the second block at any velocity and with a mass of
    any number that is a power of 100 (100^n: 1, 100, 10000, etc.). This program can also be used to simulate any combination of 
    mass and velocity for the two blocks as well as counting the number of collisions that are present during the simulation

How do I run this?

    This code was primarily run through VSCode's python extension during development, but can be ran through most python interpreters.
    This software does require that pygame is to be installed on the device.

Bugs?

    This simulation contains several bugs when being brought to a large scale. Any mass that is over 10,000 is inconsistent and usually
    incorrect. To figure out a solution, collision tolerance was tested but was sadly unsuccessful. Due to the simulations dependence on
    the GUI, some arguments are impossible to execute.