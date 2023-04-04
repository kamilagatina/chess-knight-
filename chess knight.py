#    На шахматной доске 8×8 стоит конь. 
#    Программа отмечает положение коня на доске и все клетки, 
#    которые бьет конь. Клетка, где стоит конь, отмечается английской буквой N,
#    клетки, которые бьет конь, отмечаются символами *, 
#    остальные клетки заполняются точками
#    На вход программе подаются координаты коня 's' на шахматной доске в шахматной нотации
#   (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), 
#    затем номеру строки (цифра от 1 до 8, снизу вверх)).


s = input()
column = ['a','b','c','d','e','f','g','h']
matrix = [['.' for _ in range(12)] for _ in range(12)] 
knight_coordinate1 = column.index(s[0])+2 
knight_coordinate2 = int(s[1])+2 
matrix[-knight_coordinate2][knight_coordinate1] = 'N'
bias1 = [-2,-2,1,1,-1,-1,2,2]
bias2 = [-1,1,2,-2,2,-2,1,-1]
for i in range(len(bias1)):
    matrix[-knight_coordinate2-bias1[i]][knight_coordinate1-bias2[i]] = '*'
for i in range(2,10):
    for j in range(2,10):
        print(matrix[i][j],end=' ')
    print()


# There is a knight on an 8×8 chessboard.
# The program marks the position of the knight on the board and all the cells,
# which the knight beats. The cage where the horse stands is marked with the English letter N,
# cells hit by the knight are marked with *,
# the rest of the cells are filled with dots
# The input to the program is the coordinates of the knight 's' on the chessboard in chess notation
# (that is, in the form e4, where the column number is written first (letter from a to h, from left to right),
# followed by the line number (a number from 1 to 8, from bottom to top)).
