"""
问题：一个大小为size*size的国际象棋正方形棋盘，请找出一种走法，使得Knighs能够在不重复的情况下遍历棋盘上所有的位置
(Knights类似中国象棋中马，只能走日字形）

解决办法：

步骤一：遍历整个棋盘上的坐标-（row，column），对每个坐标，找出其可到达的其他坐标，并在两点间建立一条边，代表这两点间可达
建立一幅图Ktgraph表示Knights在每个点可行走的位置
步骤二：使用深度优先搜索算法，找出一条长度为row*column-1的路径

"""
from pythonds.graphs.adjGraph import  Graph,Vertex

def knightGraph(bdSize):
    """
    建立KtGraoh
    """
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)  # 获取当前的NodeId
            newPositions = genLegalMoves(row, col, bdSize)  # 返回可移动位置的列表
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)  # 产生可移动结点的NodeId
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize+col   # 给定行列坐标（row，col），产生该节点的Node ID

def genLegalMoves(x, y, bdSize):
    """
     找出可移动的位置
    """
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]    # 日字形走法以坐标形式表示共有8种offset
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):  # 理论上若棋盘无限大，每个Knights结点对应着8种走法，但棋盘是有限的，故要判断可移动的位置是否在棋盘合法坐标内

    if x >= 0 and x < bdSize:
        return True
    else:
        return False


"""
深度优先搜索
"""

