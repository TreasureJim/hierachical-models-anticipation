# What is this 

A simulation of forklifts creating paths to their respective containers by anticipating each others movements in the A-Star algorithm. 

# Main Loop 

## Start 
1. Forklifts start in their starting points
2. Containers are spawned randomly in a grid

## Loop

1. Each forklift is assigned a random crate to fetch and place in their drop-off zones 
2. An initial path is created using pathfinding to the crate
3. Each path is checked to see if it will coincide with any of the other forklift's paths
	a) if it does then the forklift changes the path to wait until the path is clear of other forklift's
4. Repeat for path back to the drop-off zone
5. Spawn new crates

# TODO

- implement algorithm for pathfinding 
- simulate steps with simpy 
