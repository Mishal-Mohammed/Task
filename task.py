first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = ''
for j in range(m):
    text = ''
    for i in range(n):
        item = matrix[i][j]
        if item.isalnum() :
            text = item
        elif item != '':
            text = ''
    text = text.strip()
    result = text
print(result)