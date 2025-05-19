import streamlit as st
import pandas as pd
import re
from random import randint


def main():
    # Load the data
    df = pd.read_excel("tables/all.xlsx")

    # Display the title
    questionField = st.empty()
    answerField = st.empty()

    while True:
        category = 1
        print()
        questionField.empty()
        answerField.empty()
        questionField.markdown(
            f"<h2 style='text-align: center; color: #eeeeee;'>Next Question?</h2>",
            unsafe_allow_html=True,
        )
        input("Press Enter to show next question...")

        qIndex = randint(0, len(df))

        # Get the question and answer
        text = df.values[qIndex][category]
        match = re.match(r'^[0-9]+\.([^=]*)(.*)$', text)
        questionText = "null"
        answerText = "null"
        if match is not None:
            questionText, answerText = match.groups()

        questionField.markdown(
            f"<h2 style='text-align: center; color: #eeeeee;'>{questionText}</h2>",
            unsafe_allow_html=True,
        )

        # Display the answer
        print()
        input("Press Enter to see the answer...")
        answerField.markdown(
            f"<h2 style='text-align: center; color: #eeeeee;'>{answerText}</h2>",
            unsafe_allow_html=True,
        )

        # Clear the previous output
        print()
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
