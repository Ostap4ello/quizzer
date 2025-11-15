import pandas as pd
import re
from random import randrange

MATH_EXPRESSION = 0
QUESTION_ANSWER = 1

TableColumnTypes = {
    MATH_EXPRESSION: {
        "column_typename": "MATH",
        # [<number>.] <expression> = <result>
        "regex": r"^([0-9]+\.)?([^=]*)(.*)$",
    },
    QUESTION_ANSWER: {
        "column_typename": "QUESTION",
        # [<number>.] <question>? -> <answer>
        "regex": r"^([0-9]+\.)?(.*\?) -\> (.*)$",
    },
}

column_type_regex = r"^.*#([A-Z_]+)$"

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

    def getColumns(self) -> list[str]:
        column_list = self._table.columns.tolist()
        return column_list

    def _getQuestionAndAnswer(self, col: int, row: int, category: int) -> tuple | None:
        entry = self._table.values[row][col]
        match = None

        match = re.match(TableColumnTypes[category]["regex"], entry)

        if match is not None:
            # Get last two groups: question and answer
            return (match.groups()[-2].strip(), match.groups()[-1].strip())
        else:
            return None

    def getRandomQuestionAndAnswer(self, col: int) -> tuple | None:
        if col < 0 or col >= len(self._table.columns):
            return None

        category_name = str(self._table.columns[col])
        category = None
        for key, value in TableColumnTypes.items():
            _ = re.match(column_type_regex, category_name)
            if _ is None:
                continue

            if value["column_typename"] == _.groups()[0]:
                category = key
                break

        if category is None:
            return None

        if self.getLen(col) == 0:
            return None

        row = randrange(0, self.getLen(col))
        return self._getQuestionAndAnswer(col, row, category)
