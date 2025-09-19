class Spreadsheet:
    def __init__(self, rows: int):
        # initialize with 0s
        self.sheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        # remove '='
        formula = formula[1:]
        left, right = formula.split('+')

        def eval_part(part: str) -> int:
            if part[0].isalpha():  # cell reference
                col = ord(part[0]) - ord('A')
                row = int(part[1:]) - 1
                return self.sheet[row][col]
            else:  # integer
                return int(part)

        return eval_part(left) + eval_part(right)