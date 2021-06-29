# RRT - Python

This repository is a python implementation of the RRT algorithm.

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