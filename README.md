# Fast Food Chain

## Algorithmic Challenges

This repository contains efficient algorithmic solutions for two distinct problems - optimizing revenue for a chain of restaurants and finding the shortest path in a tower quest. 

## Question 1: Fast Food Chain

The `restaurantFinder` function identifies the optimal sites to open restaurants by evaluating potential revenue while adhering to specified constraints using a dynamic programming approach. The objective is to maximize the total revenue obtained from opening restaurants at certain sites, while maintaining a minimum distance `d` between any two restaurant sites.

## Question 2: Climb King

The `FloorGraph` class along with its method `climb` aims to find the shortest path through a tower (modeled as a graph), where a key must be collected while navigating from a starting point to one of the specified exits. The graph is constructed to model paths and keys on the floor, and a variation of Dijkstra's algorithm is applied to determine the shortest path while ensuring a key is obtained during the traversal.

## Usage

Each question is solved in a dedicated function or class and can be utilized independently. Example usages and test cases are provided within the script to showcase the functionality and utility of the developed solutions.

## Time and Space Complexity

Detailed time and space complexity analyses are provided in the function and method docstrings, ensuring transparency regarding the computational efficiency of the solutions.
