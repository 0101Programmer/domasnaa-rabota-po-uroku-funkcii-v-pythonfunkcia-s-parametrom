def get_matrix(n, m, value):
    matrix = []
    for i in range(int(n)):
        sub_matrix = []
        for j in range(int(m)):
            sub_matrix.append(value)
        matrix.append(sub_matrix)
        sub_matrix.append(value)
    return matrix


matrix = get_matrix('3', '4', '45')
print(f'Result: {matrix}')
