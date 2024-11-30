
# Pacman AI Search Agent

This repository contains an implementation of search algorithms (DFS, BFS, UCS) in the context of the Pacman AI project. The goal is to control Pacman in a maze using different search strategies, including Depth-First Search (DFS), Breadth-First Search (BFS), and Uniform Cost Search (UCS).


The project was originally developed for educational purposes as part of UC Berkeley's CS 188 course on Artificial Intelligence. For more information on the project, visit the official [UC Berkeley AI Project Overview](https://ai.berkeley.edu/project_overview.html). 

You can also view https://github.com/raihanewubd/Pacman

## Algorithms Implemented

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Uniform Cost Search (UCS)**

These search algorithms can be used to find the shortest path to a goal (or across multiple goals) in a maze, depending on the strategy used.


## Running the Game

We can run the Pacman game with the search agent by using the following commands. Each search algorithm (DFS, BFS, and UCS) can be selected via the -a fn= algorithm flag.

1. For Depth-First Search (DFS):
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
2. For Breadth-First Search (BFS):
    ```bash
    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
3. For Uniform Cost Search (UCS):
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
Replace mediumMaze with other maze layouts like tinyMaze, bigMaze, etc. for testing with different complexities.

## Time Comparison of Search Algorithms

| Algorithm | Big Maze | Medium Maze | Small  Maze |
|   :---:   |     :---:      |          :---: |          :---: |
| BFS   | 0.035996 seconds     | 0.008980 seconds   | 0.004038 seconds |
| DFS   | 0.009036 seconds    | 0.005739 seconds  | 0.002180 seconds|
| UCS  | 0.013265 seconds   | 0.006808 seconds |0.003454 seconds|

## ScreenShots:

![Screenshot 2024-12-01 014358](https://github.com/user-attachments/assets/404d6a9a-64d3-4e8d-8575-e6aeca1e90b4)

![Screenshot 2024-12-01 014735](https://github.com/user-attachments/assets/f7851a04-855f-4eb7-9f3c-89737f6af6c3)
