from time import sleep
from numpy import empty
import streamlit as st


class Display:
    def __init__(self):
        self._title = st.empty()
        self._questionField = st.empty()
        self._answerField = st.empty()
        self._button = st.empty()

    def setQuestion(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._questionField.write(f_s, unsafe_allow_html=True)

    def setAnswer(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._answerField.write(f_s, unsafe_allow_html=True)

    def setTitle(self, s):
        self._title.title(s)

    def setButton(self, s, on_click=None):
        self._button.button(s, on_click=on_click)

    def sleepUntillButtonIsPressed(self, s):
        st.session_state.clicked = False

        def setState():
            st.session_state.clicked = True
            print("a")

        self.setButton(s, on_click=setState)
        while False:
            sleep(0.5)
            if st.session_state.clicked is True:
                return;

    def clearTitle(self):
        self._title.empty()

    def clearQuestion(self):
        self._questionField.empty()

    def clearAnswer(self):
        self._answerField.empty()

    def clearButton(self):
        self._button.empty()
