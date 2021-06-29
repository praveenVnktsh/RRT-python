import numpy as np

class Node:
    def __init__(self, x, y):

        self.connected = False
        self.connectedTo = []
        self.x = x
        self.y = y
    
    def connect(self, node):
        self.connectedTo.append(node)

    def tolist(self):
        return np.array([self.x, self.y])


def getNeighbourNodes(node, nodes, sampleStepSize = 5.1):
    nodelist = [x.tolist() for x in nodes]
    diff = node.tolist() - np.array(nodelist)
    distances = np.linalg.norm(diff,  axis = 1)
    
    indices = [i for i in range(len(distances))]
    indices = [x for _,x in sorted(zip(distances, indices))]
    numpick = np.sum((distances < sampleStepSize * np.sqrt(2)).astype(int))
    if numpick == 0:
        return 1, []
    
    indices = indices[:numpick]

    return 0, [nodes[i] for i in indices]

def getNearestNode(node, nodes, verbose = False):
    occupiednodelist = np.array([x.tolist() for x in nodes])
    coorddiff = node.tolist() - occupiednodelist
    
    distances = np.linalg.norm(coorddiff, axis = 1)
    nodeToConnect = nodes[np.argmin(distances)]

    if verbose:
        indices = [i for i in range(len(distances))]
        indices = [x for _,x in sorted(zip(distances, indices))]
        print(indices, distances)


    return nodeToConnect