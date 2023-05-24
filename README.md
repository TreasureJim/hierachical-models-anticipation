# What is this 

This is created to investigate the `simpy` library for hierarichical anticipatory models. 

Initially I misunderstood the point of the library and tried creating a more complex project with graphics however I now see this isn't the point of the library. All graphics work can be found in the `graphics-test` folder.

Running the `main.py` folder will print out a simulation of the below description using the simpy library

# Simulation

Simulation of forklifts in a warehouse navigating around a grid structure of containers which they pick up. New containers are dropped off at the "pickup zone" to be stored in the grid and some crates (called "delivery crates") are marked to be taken to the "dropoff zone". Crates are to be prioritised in the order that the command is made. 
