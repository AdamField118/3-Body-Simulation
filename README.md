# 3-Body-Simulation
Goal:

Test my understanding with libraries

Inspiration:

My CS major friends, Rio and Jacob, along with an amazing YouTube video by Sebastian Lague https://www.youtube.com/watch?v=8nIB7e_eds4

Project:

An animation of the 3-body-problem in python

Steps:
1. Define the problem further
2. Decide which libraries will be best
    - Want interactive element
        - Maybe mass, radius, maybe orbit distance, of planets chosen by person who initilizes the code
3. Define a structure for my code
    - Utlize classes and functions
4. start coding!
5. user test
6. turn in

Research:  

My initial understanding is that I just need to define three objects with mass and radius, give them an initial position and velocity, and let the simulation evolve over time based off simply Newton's Universal Law of Gravitation. In practicality that is probably naive, there is a reason that the three body problem is famous. This section is for my research on numerical solutions of the problem.

I start with a quick google search for resources, the stop at my personal textbook library wasn't fruitful so I need to go online:  
    As far as I can tell, my initial reactio was right, define my variables, make equations of motions for my three bodies, give them some initial velocity, watch it evolve.  
    I also found resources for helping me create a more suffisticated solutions with tools I learned last term like Hamiltonians.

Mathematical desciption of the system:

Let there be three planets of position $r_0$, $r_1$, and $r_2$  
Using newton's universal law of gravitation, acceleration due to gravity on planet 0 is:  
$$\Vec{\ddot{r}}_0=-Gm_2\frac{r_0-r_1}{|r_0-r_1|^3}-Gm_3\frac{r_0-r_2}{|r_0-r_2|^3}$$,  
acceleration due to gravity on planet 1 is:  
$$\ddot{r}_1=-Gm_0\frac{r_1-r_0}{|r_1-r_0|^3}-Gm_3\frac{r_1-r_2}{|r_1-r_2|^3}$$,  
and acceleration due to gravity on planet 2 is:  
$$\ddot{r}_2=-Gm_0\frac{r_2-r_0}{|r_2-r_0|^3}-Gm_1\frac{r_2-r_1}{|r_2-r_1|^3}$$  

Now I am interested in doing this in Hamiltonians as well, in case I find it easier to code it this way, I likely will code both mathematical desciptions.
So again let there be three planets of position $r_0$, $r_1$, and $r_2$  
