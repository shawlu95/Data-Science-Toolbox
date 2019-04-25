# Genetic Programming
A simple demo of genetic programming concepts with candidate functions of affine transformation and conditional statement.

## Elemental Functions
The module includes limited types of operation. Those operations can approximate linear function, quadratic function, and polynomial function. As the function gets more complex, the evolution takes longer time to make progress. Tune parameters as necessary to speed up evolution.
* Addition
* Subtraction
* Multiplication
* If statement
* Is greater condition

## Tree Representation
To represent function as a tree, three types of nodes are necessary. The tree is defined in recursive manner. Each branch of the tree must end with at least one constant or parameter.
* Operation node: perform one of the operations available. The operation is performed on the values returned by its child nodes.
* Parameter node: return a parameter
* Constant node: return a constant.

## Evolution Parameters
* rankfunction: The function used on the list of programs to rank them from best to worst.
* mutationrate: The probability of a mutation, passed on to mutate.
* breedingrate: The probability of crossover, passed on to crossover.
* popsize: The size of the initial population.
* probexp: The rate of decline in the probability of selecting lower-ranked programs. A higher value makes the selection process more stringent, choosing only programs with the best ranks to replicate.
* probnew: The probability when building the new population

## Getting Started
Run [tutorial.ipynb](/tutorial.ipynb) to see how each function in the [genetic.py](/genetic.py) module is defined. Test each function with test-case to understand the concepts behind genetic programming.

Run [example.ipynb](/example.ipynb) to apply genetic programming to approximate a simple quadratic function. Experiment with different truth function to see how genetic program reacts. Adjust evolution parameters as necessary.
