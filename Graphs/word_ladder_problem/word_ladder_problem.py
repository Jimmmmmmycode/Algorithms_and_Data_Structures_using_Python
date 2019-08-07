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



