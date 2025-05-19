import wrappers.display
import pandas as pd
import re
from random import randint


def main():
    # Load the data
    df = pd.read_excel("tables/all.xlsx")

    disp = wrappers.display.Display()

    while True:
        category = 1

        disp.setQuestion("Next Question ?")
        disp.clearAnswer()

        print()
        input("Press Enter to show next question...")

        qIndex = randint(0, len(df))

        # Get the question and answer
        text = df.values[qIndex][category]
        match = re.match(r'^[0-9]+\.([^=]*)(.*)$', text)
        questionText = "null"
        answerText = "null"
        if match is not None:
            questionText, answerText = match.groups()

        disp.setQuestion(questionText)

        # Display the answer
        print()
        input("Press Enter to see the answer...")
        disp.setAnswer(answerText)

        # Clear the previous output
        print()
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
