marks = [[1,2,3],[4,5,6],[7,8,9]]
rotate = [[False for i in range(len(marks[0]))] for j in range(len(marks))]
for row, items in enumerate(marks):
    for col, val in enumerate(items):
        rotate[col][row] = val
for row in marks:
    print(row)

for row in rotate:
    print(row)
