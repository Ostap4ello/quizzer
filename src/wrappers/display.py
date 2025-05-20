import streamlit as st

class Display():
    def __init__(self):
        self._title = st.title("")
        self._questionField = st.empty()
        self._answerField = st.empty()

    def setQuestion(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._questionField.write(f_s, unsafe_allow_html=True)

    def setAnswer(self, s: str):
        f_s = f"<h2 style='text-align: center; color: #eeeeee;'>{s}</h2>"
        self._answerField.write(f_s, unsafe_allow_html=True)

    def setTitle(self, s):
        self._title.title(s)

    def clearTitle(self):
        self._title.title("")

    def clearQuestion(self):
        self._questionField.empty()

    def clearAnswer(self):
        self._answerField.empty()
