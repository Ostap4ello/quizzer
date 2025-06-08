import streamlit as st

pg = st.navigation([
    st.Page("pages/quiz.py", title="Quiz", icon=":material/sports_esports:"),
    st.Page("pages/settings.py", title="Settngs", icon=":material/settings:"),
    st.Page("pages/about_me.py", title="About me", icon=":material/favorite:"),
])
pg.run()
