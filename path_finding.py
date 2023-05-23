"""
Implementation of A-Star algorithm

NOTE: Will not use A-Star algorithm and will use an algorithm made specifically for the set positioning of the crates which will be faster

NOTES:
Each step picks a node with the lowest f value
f = g + h
g is movement cost from starting point to the given square
h is estimated movement cost from given square to final destination 

`h` Techniques
approximation


Algorithm:
1. Initialize the open and close list
2. Add starting node to open list (f value = 0)
3. while open list not empty 
    a) q = node in it with lowest f value 
    b) pop q off open list
    c) generate 4 successors (surrounding nodes) with parent set to q
    d) loop sorrouding successors
        i) if successor is goal, stop search
        ii) compute g and h for successor
            successor.g = q.g + distance between successor and q (always 1 in this case)
            successor.h = (discussed later)
        iii) if node with same position (?) in open or closed list with lower f value then skip the sucessor
        iv) add successor to open list
    e) push q to closed list
"""


def find_path(start: tuple[int, int], end: tuple[int, int]):
    """
    Finds a path between `start` and `end`
    """
