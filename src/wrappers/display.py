import streamlit as st

class DisplayState():
    INIT = 0
    SHOWING_QUESTION = 1
    SHOWING_ANSWER = 2
    count = 3

class Display():
    def __init__(self):
        self._state = DisplayState.INIT
        self.reset()

    def reset(self):
        self._title = st.empty()
        self._questionField = st.empty()
        self._answerField = st.empty()
        self._button = st.empty()

    def getState(self):
        return self._state

    def nextState(self):
        self._state = (self._state + 1) % DisplayState.count

    def setTitle(self, s):
        self._title.title(s)

    def setQuestion(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._questionField.write(f_s, unsafe_allow_html=True)

    def setAnswer(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._answerField.write(f_s, unsafe_allow_html=True)

    def setButton(self, s: str, f=None):
        self._button.empty()
        self._button.button(s,on_click=f)

    def clearTitle(self):
        self._title.title("")

    def clearQuestion(self):
        self._questionField.empty()

    def clearAnswer(self):
        self._answerField.empty()

    def clearButton(self):
        self._button.clear()
