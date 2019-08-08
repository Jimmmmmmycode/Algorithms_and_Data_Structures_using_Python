"""
将单词 “FOOL” 转换为单词 “SAGE
每一步只能将一个字变成另一个字

FOOL
POOL
POLL
POLE
PALE
SALE
SAGE

计算起始字转换为结束字的最少步骤

"""

from pythonds.graphs.adjGraph import Graph,Vertex
from pythonds.basic.queue import Queue

def BulidGraph(wordFile):
    """
     :param wordFile: 传入一个记录所有相同长度的单词的列表
    :return: 返回按照特性连接的图
    """
    g=Graph()
    d={}   # 以三个相同字母+_为键，包含这三个字母的单词为值，记录wordFile中仅有一个字母不同的单词的集合，便于利用该字典添加边
           # addEdge的原则：当两个相同长度单词间仅有一个字母不同时，添加一条无向边
    words=open(wordFile,'r') # words-包含wordFile中所有单词的列表
    for lines in words:
        word=lines[:-1]  # 提取掉'\n'
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]  # 注意这里一个key可能对应着多个word，所以word要存储在列表中
    """提取绘图字典d"""
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g


"""
BFS-广度优先搜索
"""
def BFS(g,start): # 给定一幅图g和一个起始节点start,在广度优先搜索过程中遍历图中所有结点，并标记它们的距离，前驱和颜色
    start.setDistance(0)#设置start结点的距离为0
    start.setPred(None)#设置start结点的前驱为None
    VertQueue=Queue()#创建一个队列用于按保存待搜索结点
    VertQueue.enqueue(start)#将start结点入队
    #循环遍历所有入队的结点
    while (VertQueue.size()>0):
        CurrentVert=VertQueue.dequeue()
        # 遍历当前搜索结点的所有邻居
        for nbr in CurrentVert.getConnections():  #.getConnections方法返回CurrentVert的所有邻居结点
            #若该邻居的颜色为白色，则其从未被搜索,对其执行入队，染色，设定距离和前驱的操作
            if (nbr.getColor()=='white'):
                nbr.setColor('grey')
                nbr.setDistance(CurrentVert.getDistance()+1)
                nbr.setPred(CurrentVert)
                VertQueue.enqueue(nbr)
        #直至CurrentVert的结点被遍历完毕，代表其邻居结点已被完全搜索，将其颜色设为黑色
        CurrentVert.setColor('black')

def Solution(V):  # 在对图以'FOOL'进行BFS后，建立了BFS Search Tree（以.Pred()为线索)，从'SAGE'开始，遍历它的Pred并直至'FOOL'（Pred为None）
    X=V
    while(X.getPred()):
        print(X.getId())
        X=X.getPred()
    print(V.getId()) # 在检测到'FOOL'.pred=None后循环退出，需增加一次打印'FOOL'

wordgraph=BulidGraph('fourletterwords.txt')
BFS(wordgraph,wordgraph.getVertex('FOOL'))
Solution(wordgraph.getVertex('SAGE'))