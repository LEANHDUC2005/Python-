def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Lst = [[1]]
        if numRows == 1: 
            return Lst
        for i in range(numRows - 1):
            newLst = Lst[i][:]
            newLst.append(1)
            for j in range(1, len(Lst[i])):
                newLst[j] = Lst[i][j-1] + Lst[i][j]
            Lst.append(newLst)
        return Lst
result = generate(3)
print(result)