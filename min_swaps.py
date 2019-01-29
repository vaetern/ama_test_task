class Matrix:
    def __init__(self, values):
        self.__values = values
        self.height = len(values)
        self.width = len(values[0])

    def items(self):
        return self.__values


def calculate_window_score(window_size: int, matrix: Matrix):
    pass


def run_test():
    table = (
        [{1: 9, 2: 27, 3: 51},
         (
             (1, 2, 3, 4, 5, 6),
             (1, 2, 3, 4, 5, 7),
             (1, 2, 3, 4, 5, 8),
             (1, 2, 3, 4, 5, 9),
             (1, 2, 3, 4, 5, 0),
             (1, 2, 3, 4, 5, 1),
         )],
        ({3: 5, 0: 0, 2: 3},
         (
             (0, 1, 0, 0, 0,),
             (0, 1, 0, 0, 0,),
             (1, 1, 1, 0, 0,),
             (0, 1, 0, 0, 0,),
             (0, 1, 0, 0, 0,),
         )),
        ({3: 6, 0: 0, 2: 5},
         (
             (0, 1, 0, 0, 5,),
             (0, 1, 0, 0, 0,),
             (1, 2, 1, 0, 0,),
         )),
    )

    for i in table:
        matrix = Matrix(i[1])
        for size in i[0]:
            answer = i[0][size]
            if calculate_window_score(size, matrix) != answer:
                print(matrix.items(),
                      f'window = {size}, calculated {calculate_window_score(size, matrix)} != {answer}')
            else:
                print(f'> passed')


# ------------------------------------
run_test()

# //end