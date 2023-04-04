s,buk= input(),['a','b','c','d','e','f','g','h']
matrix = [['.' for _ in range(12)] for _ in range(12)]
i1 = buk.index(s[0])+2
i2 = int(s[1])+2
matrix[-i2][i1] = 'N'
t1 = [-2,-2,1,1,-1,-1,2,2]
t2 = [-1,1,2,-2,2,-2,1,-1]
for i in range(len(t1)):
    matrix[-i2-t1[i]][i1-t2[i]] = '*'
for i in range(2,10):
    for j in range(2,10):
        print(matrix[i][j],end=' ')
    print()
