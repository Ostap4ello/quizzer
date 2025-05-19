import wrappers.display
import wrappers.table


def main():
    # Load the data
    table = wrappers.table.QuizTable("tables/all.xlsx")

    disp = wrappers.display.Display()

    while True:
        category = wrappers.table.MATH_EXPRESSION
        col = 1
        answerText = questionText = ""

        disp.setQuestion("Next Question ?")
        disp.clearAnswer()

        print()
        input("Press Enter to show next question...")

        _ = table.getRandomQuestionAndAnswer(col, category)
        if _ is not None:
            questionText, answerText = _

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
