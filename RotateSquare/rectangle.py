class Rectangle:
    def __init__(self, matrix):
        self.rectangle = matrix
        self.num_rows = len(matrix)
        self.num_columns = len(matrix[0])

    def display(self):
        for row in self.rectangle:
            print(row)
    
    def rotate_clockwise(self):
        rotation = []
        for idx1 in range(self.num_columns):
            new_row = []
            for idx2 in range(self.num_rows - 1, -1, -1):
                new_row.append(self.rectangle[idx2][idx1])
            rotation.append(new_row)
        return rotation

    def rotate_counter_clockwise(self):
        rotation = []
        for idx1 in range(self.num_columns - 1, -1, -1):
            new_row = []
            for idx2 in range(self.num_rows):
                new_row.append(self.rectangle[idx2][idx1])
            rotation.append(new_row)
        return rotation