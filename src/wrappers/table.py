import pandas as pd
import re
from random import randint

# enum: column types
MATH_EXPRESSION = 0

# regexes
_MATH_EXPRESSION_REGEX = r'^[0-9]+\.([^=]*)(.*)$'

class QuizTable:
    def __init__(self, table_exel):
        self._table = pd.read_excel(table_exel)

    def getLen(self, col):
        row = 0
        max_row = len(self._table)
        while True:
            if row == max_row or pd.isna(self._table.values[row][col]):
                return row
            row += 1

    def getQuestionAndAnswer(self, col: int, row: int, category: int):
        entry = self._table.values[row][col]
        match = None
        if category == MATH_EXPRESSION:
            match = re.match(_MATH_EXPRESSION_REGEX, entry)
        else:
            print('Unsupported cathegory')

        if match is not None:
            return match.groups()
        else:
            return None

    def getRandomQuestionAndAnswer(self, col: int, category: int):
        row = randint(0, self.getLen(col))
        return self.getQuestionAndAnswer(col, row, category)

