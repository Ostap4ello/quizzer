import streamlit as st
from wrappers.table import QuizTable, TableColumnTypes


class DisplayState:
    GREETING = 0
    SHOWING_QUESTION = 1
    SHOWING_ANSWER = 2

    stateCount = 3

    def __init__(self):
        self._state = DisplayState.GREETING
        # self.reset()

    def getState(self):
        return self._state

    def nextState(self):
        self._state = (self._state + 1) % DisplayState.stateCount


glob = st.session_state

# Get QuizTable

if "retries" not in st.session_state:
    st.session_state.retries = 0

if "quiztable" not in st.session_state:
    st.session_state.quiztable = QuizTable("tables/all.xlsx")

try:
    assert isinstance(glob.quiztable, QuizTable)
except AssertionError:
    # st.error("Error: 'quiztable' in session state is not a QuizTable instance!")
    pass

# Get Display
if "disp" not in st.session_state:
    st.session_state.disp = DisplayState()

try:
    assert isinstance(glob.disp, DisplayState)
except AssertionError:
    # st.error("Error: 'disp' in session state is not a Display instance!")
    pass

disp = glob.disp
table = glob.quiztable


# Page

category = TableColumnTypes.MATH_EXPRESSION
col = 0

if disp.getState() == DisplayState.GREETING:
    q, a = "Next Question ?", ""

elif disp.getState() == DisplayState.SHOWING_QUESTION:
    _ = table.getRandomQuestionAndAnswer(col, category)
    if _ is not None:
        glob.qaPair = _
        q, a = glob.qaPair[0], "..."
    else:
        if glob.retries < 5:
            glob.retries += 1
            st.rerun()
        st.error("Error: Could not fetch question and answer from the table!")
        glob.retries = 0
        q, a = "Error fetching question", ""


elif disp.getState() == DisplayState.SHOWING_ANSWER:
    q, a = glob.qaPair

else:
    q, a = "", ""


st.title("Quiz Time!")

style_attr = "style='text-align: center; font-size: 64px; color: #eeeeee; height: 150px;'"
f_s = f"<h1 {style_attr} >{q}</h1>"
st.html(f_s)
f_s = f"<h1 {style_attr} >{a}</h1>"
st.html(f_s)

st.button("Next", on_click=disp.nextState, key="next_button")
