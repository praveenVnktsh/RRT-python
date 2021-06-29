from utils import scaleAndShow
import cv2
import numpy as np
from node import Node, getNearestNode, getNeighbourNodes
import random


def sampleGrid(mask, step = 5, viz = True):
    h, w = mask.shape
    x = np.arange(0, w - 1, step).astype(int)
    y = np.arange(0, h - 1, step).astype(int)

    indices = np.ix_(y,x)
    temp = mask.copy()
    temp[indices] = 128
    temp[mask == 0] = 0
    indices = temp == 128

    if viz:
        temp = mask.copy()
        temp[indices] = 128
        scaleAndShow(temp, 'ab', height = 600)
    y, x = np.where(indices == True)
    return x, y, indices


mask = np.ones((500, 500), dtype=np.uint8) * 255
x, y, indices = sampleGrid(mask, step = 5, viz = False)
mask[indices] = 0
nodes = []
for point in list(zip(y, x)):
    nodes.append(Node(point[1], point[0]))


unoccupiedNodes = nodes.copy()


occupiedNodes = [getNearestNode(Node(134, 304), nodes)]
unoccupiedNodes.remove(occupiedNodes[0])
cv2.circle(mask, occupiedNodes[0].tolist(), 1, 128, 1)
complete = False
i = 0
height = 600
waitkey = 1
scaleAndShow(mask, 'a', height = height, waitkey=0)
while not complete:

    # unoccupied.pop(np.random.randint(0, len(unoccupied)))
    temp = mask.copy()
    temp = np.stack((temp, temp, temp), axis= 2)

    directionNode : Node = random.choice(unoccupiedNodes)

    nodeToConnect = getNearestNode(directionNode, occupiedNodes)
    ret, neighbourNodes = getNeighbourNodes(nodeToConnect, unoccupiedNodes)
    if ret:
        continue
    extensionNode = getNearestNode(directionNode, neighbourNodes)

    cv2.circle(temp, directionNode.tolist(), 3, (0, 255, 0), -1)
    scaleAndShow(temp, 'a', waitkey = waitkey, height = height)


    cv2.circle(temp, nodeToConnect.tolist(), 3, (255, 0, 0), -1)
    scaleAndShow(temp, 'a', waitkey = waitkey, height = height)

    for node in neighbourNodes:
        cv2.circle(temp, node.tolist(), 2, (0, 0, 255), -1)
    scaleAndShow(temp, 'a', waitkey = waitkey, height = height)

    cv2.circle(temp, extensionNode.tolist(), 2, (0, 255, 0), -1)
    scaleAndShow(temp, 'a', waitkey = waitkey, height = height)


    unoccupiedNodes.remove(extensionNode)
    nodeToConnect.connect(extensionNode)

    ax, ay = extensionNode.tolist()
    bx, by = nodeToConnect.tolist()
    occupiedNodes.append(extensionNode)
    

    cv2.circle(mask, extensionNode.tolist(), 2, 128, -1)
    cv2.line(mask, (ax, ay), (bx, by),  0, 1)

    
    scaleAndShow(mask, 'a', waitkey = 10, height = height)
    i += 1

    if i == 1000:
        complete = True