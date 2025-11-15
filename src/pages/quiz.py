import streamlit as st
from wrappers.table import QuizTable, TableColumnTypes


display_state = {
    "GREETING": 0,
    "SHOWING_QUESTION": 1,
    "SHOWING_ANSWER": 2,
}


def next_display_state(current_state: int) -> int:
    if current_state == display_state["GREETING"]:
        return display_state["SHOWING_QUESTION"]
    elif current_state == display_state["SHOWING_QUESTION"]:
        return display_state["SHOWING_ANSWER"]
    elif current_state == display_state["SHOWING_ANSWER"]:
        return display_state["GREETING"]
    else:
        return display_state["GREETING"]


glob = st.session_state

# Get QuizTable

if "quiztable" not in glob:
    glob.quiztable = QuizTable("tables/all.xlsx")

if "display_state" not in glob:
    glob.display_state = display_state["GREETING"]

table: QuizTable = glob.quiztable

# Page
st.title("Quiz Time!")
st.markdown("##")  # Spacer

# Quiz body
if "chosen_column" not in st.session_state:
    if len(table.getColumns()) > 1:
        st.info("Please select a category to start the quiz.")
    else:
        st.session_state.chosen_column = 0

with st.container():
    if glob.display_state == display_state["GREETING"]:
        q, a = "Next Question ?", ""
        glob.display_state = next_display_state(glob.display_state)

    elif glob.display_state == display_state["SHOWING_QUESTION"]:
        _ = None
        for retries in range(5):
            _ = table.getRandomQuestionAndAnswer(st.session_state.chosen_column)
            if _ is not None:
                break

        if _ is not None:
            glob.qaPair = _
            q, a = glob.qaPair[0], "..."
            glob.display_state = next_display_state(glob.display_state)
        else:
            st.error("Error: Could not fetch question and answer from the table!")
            q, a = (
                "Error fetching question",
                f"chosen column idx: {st.session_state.chosen_column}",
            )

    elif glob.display_state == display_state["SHOWING_ANSWER"]:
        q, a = glob.qaPair
        glob.display_state = next_display_state(glob.display_state)

    else:
        q, a = "", ""
        glob.display_state = display_state["GREETING"]

    style_attr = "style='text-align: center; font-size: 64px; height: 150px;'"
    f_s = f"<h1 {style_attr} >{q}</h1>"
    st.html(f_s)
    f_s = f"<h1 {style_attr} >{a}</h1>"
    st.html(f_s)

st.button(
    "Next",
    key="next_button",
    use_container_width=True,
    type="primary",
)

st.markdown("##")  # Spacer

# Category selection
with st.container(border=True) as c:
    column_list = table.getColumns()
    if len(column_list) > 1:

        grid_full_rows = int(len(column_list) ** 0.5)
        grid_full_cols = len(column_list) // grid_full_rows
        grid_nonfull_cols = len(column_list) % grid_full_rows

        button_index = 0

        cols = st.columns([0.7, 0.3])
        with cols[0]:
            st.markdown("**Select Category:**")
        with cols[1]:
            if st.button(
                "Reset Category", key="reset_category_button", use_container_width=True
            ):
                if "chosen_column" in glob:
                    del glob.chosen_column
                    glob.display_state = display_state["GREETING"]
                    st.rerun()

        for r in range(grid_full_rows):

            cols = st.columns(grid_full_cols)
            for c in cols:
                with c:
                    col_name = column_list[button_index]
                    if st.button(
                        col_name,
                        key=f"col_button_{button_index}",
                        use_container_width=True,
                    ):
                        glob.chosen_column = button_index
                        glob.display_state = display_state["GREETING"]
                        st.rerun()
                    button_index += 1

        if grid_nonfull_cols > 0:

            cols = st.columns(grid_nonfull_cols)
            for c in cols:
                with c:
                    col_name = column_list[button_index]
                    if st.button(
                        col_name,
                        key=f"col_button_{button_index}",
                        use_container_width=True,
                    ):
                        glob.chosen_column = button_index
                        glob.display_state = display_state["GREETING"]
                        st.rerun()
                    button_index += 1
