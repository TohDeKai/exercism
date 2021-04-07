'''
Psuedo-Code
1. Create a list
2. Add matrix into nested list whereby its [[x,y],[a,b]]
3. Extract row/column according to index
'''

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_string = self.matrix_string.split('\n')
        self.matrix = []
        for row in self.matrix_string:
            self.matrix.append(row.split(' '))
        
        

    def row(self, index):
        row_list = []
        for i in self.matrix[index-1]:
            row_list.append(int(i))
        return row_list

    def column(self, index):
        column_list = []
        for row in self.matrix:
            column_list.append(int(row[index-1]))
        return column_list


