import streamlit as st
from wrappers.display import Display, DisplayState
from wrappers.table import QuizTable, TableColumnTypes

if "quiztable" not in st.session_state:
    st.session_state.quiztable = QuizTable("tables/kviz.xlsx")

if "disp" not in st.session_state:
    st.session_state.disp = Display()

glob = st.session_state
disp =  st.session_state.disp
table = glob.quiztable

category = TableColumnTypes.MATH_EXPRESSION
col = 1

disp.reset()
disp.setButton("Next", disp.nextState)

if disp.getState() == DisplayState.INIT:
    disp.setQuestion("Next Question ?")
    disp.setAnswer("")

    _ = table.getRandomQuestionAndAnswer(col, category)
    if _ is not None:
        glob.questionText, glob.answerText = _
    else:
        disp._state = DisplayState.INIT
        st.rerun()

elif disp.getState() == DisplayState.SHOWING_QUESTION:
    disp.setQuestion(glob.questionText)
    disp.setAnswer("?")

elif disp.getState() == DisplayState.SHOWING_ANSWER:
    disp.setQuestion(glob.questionText)
    disp.setAnswer(glob.answerText)

else:
    pass
