# quizzer

Simple question-answer quiz with streamlit frontend.

## Usage:

0. put table with equasions like `<expression> = <result>` in 2nd column into ./tables/ and name it all.xlsx
1. setup venv, install requirements from ./requirements.txt, enter venv
2. run `streamlit run src/main.py`
3. frontend will be opened in new browser tab, press enter in console to move to each step, <Ctrl-C> to stop

### Disclaimer: 

this version was made in rush, so what it does is:
- load ./tables/all.xlsx;
- load and parse equasions from 2nd col;
- show random equasions in streamlit frontend
- uses in-console prompts for each step
