#括号匹配
from pythonds.basic.stack import Stack  #import一个stack
def ParChecker(symbolString):  #检测括号的函数，参数为一个全为括号的字符串

    checktool=Stack()  # 用于括号检测的栈

    balanced=True  #balanced作为括号是否匹配的检测值，一开始被设为True

    index=0 # 用于作为下标从从左往右访问symbolString中的括号

    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=='(':
            checktool.push(symbol)  # 如果symbol是左括号，将其压入栈中
        else:
            if checktool.isEmpty(): # 若在未检测到最后一个闭括号时检测栈已经为空，则证明不匹配，balanced设定为False
                balanced=False
            else:
                checktool.pop()  # 若栈非空，则弹出一个'（'作为匹配
        index = index+1

#当循环结束时候，有三种情况，第一，若完全匹配，此时栈为空。balanced=True
#第二，若不完全匹配，（1）后括号有剩余，栈为空，balanced==False
#（2）后括号匹配完成但前括号有剩余，栈非空，balanced=True

    if balanced and checktool.isEmpty(): #由上述分析可知，只有当balanced=True且栈为空时，才代表括号完全匹配
        return True
    else:
        return False

#测试代码

print(ParChecker('((()))'))
print(ParChecker('(()'))
print(ParChecker('((()((())())))'))
