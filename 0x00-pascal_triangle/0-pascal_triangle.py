def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        current_row = [1] * (i + 1)  # Start with 1 at the beginning

        for j in range(1, i):
            current_row[j] = prev_row[j - 1] + prev_row[j]

        triangle.append(current_row)

    return triangle

