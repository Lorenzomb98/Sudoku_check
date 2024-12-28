sudoku = []
counter = 1
while counter <=9:
    row = list(input(f"Please enter row({counter}): "))
    sudoku.append(row)
    counter += 1

inconformity = 0

for row in sudoku:
    for i in row:
        if row.count(i) > 1:
            inconformity += 1


for i in range(9):
    column = []
    for row in sudoku:
        column.append(row[i])
    for j in column:
        if column.count(j) > 1:
            inconformity += 1 


for x in range(3):
    i1 = 0
    i2 = 1
    i3 = 2
    iterators = [0,1,2]
    for y in range(3):
        square = []
        for i in range(3):
            square.append(sudoku[i1][i])
            square.append(sudoku[i2][i])
            square.append(sudoku[i3][i])
        for s in square:
            if square.count(s) > 1:
                inconformity += 1
        i1 += 3
        i2 += 3
        i3 += 3
    for i in iterators:
        iterators[i] += 3


if inconformity != 0:
    print("No")
else:
    print("Yes")

