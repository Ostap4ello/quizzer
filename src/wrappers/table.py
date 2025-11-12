import pandas as pd
import re
from random import randint

class TableColumnTypes:
    MATH_EXPRESSION = 0
    count = 1;

# regexes
_MATH_EXPRESSION_REGEX = r'^([0-9]+\.)?([^=]*)(.*)$'

class QuizTable:
    def __init__(self, table_exel):
        self._table = pd.read_excel(table_exel)

    def getLen(self, col):
        row = 0
        max_row_count = len(self._table.values)
        while True:
            if row == max_row_count or pd.isna(self._table.values[row][col]):
                return row
            row += 1

    def getQuestionAndAnswer(self, col: int, row: int, category: int) -> tuple | None:
        entry = self._table.values[row][col]
        match = None
        if category == TableColumnTypes.MATH_EXPRESSION:
            match = re.match(_MATH_EXPRESSION_REGEX, entry)
        else:
            print('Unsupported cathegory')
            return None

        if match is not None:
            return (match.groups()[-2].strip(), match.groups()[-1].strip())
        else:
            print('No match found')
            return None

    def getRandomQuestionAndAnswer(self, col: int, category: int) -> tuple | None:
        row = randint(0, self.getLen(col) - 1)
        return self.getQuestionAndAnswer(col, row, category)

