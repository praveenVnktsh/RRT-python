# RRT - Python

This repository is a python implementation of the RRT (Rapidly Exploring Random Tree) algorithm.
This algorithm is used extensively in path planning in robotics applications as a computationally inexpensive method to determine an approximately optimal path between any two points given a set of constraints.

The following is a pseudo-code of the implementation:

```python
start = a
goal = b

while not reached:   
    directionNode = sample(unoccupied_nodes)
    nodeToExtend = closestNode(directionNode, unoccopied_node)
    neighbours = nearestUnoccupiedNeighbours(nodeToExtend)
    nodeToExtend.connect(closestNode(directionNode, neighbours))
```

Here is the algorithm exploring a large open space without any goal.

![](exploration.gif)


Note that the step size is quite small, and is fixed. This can be easily changed to explore a lot faster.
