# quizzer

Simple question-answer quiz with streamlit frontend.

## Old Disclaimer: Things We Said When We Were Very Stressed (previousely just 'Disclaimer') (You may skip it)

> this version was made in rush, so what it does is:
> - load ./tables/all.xlsx;
> - load and parse equasions from 2nd col; (NOTE: yeah, we didn't parse the first col, back then)
> - show random equasions in streamlit frontend
> - uses in-console prompts for each step

**NOTE:** That (first) version was made in a panic, and has since been maintained with relative, almost worrying calm, actually, so next versions (firstly) exist and (secondly) differ from that version.

## Functionality

- loads questions and answers from excel table (tables/all.xlsx)
- shows questions in streamlit frontend with (now) some buttons to play with
- supports multiple columns to choose from

## Usage:

0. Prepare tables/all.xlsx:
    - HEADER: First row is always a header. It's format should be `<name><type>`, where:
        - `<name>` is of the name you give to this cathegory of questions (e.g. "Math", "History", etc)
        - `<type>` is either "#QUESTION" or "#MATH". This determines how values of the column will be parsed.
    - COLUMN VALUES: All next rows are values of the column. Their format depends on the type specified in header:
        - for `#QUESTION` type: `<question>? -> <answer>`, where:
            - `<question>` is the question text
            - `<answer>` is the answer text
        - for `#MATH` type: `<equasion> = <answer>`, where:
            - `<equasion>`: a mathematical equasion (question) to be evaluated
            - `<answer>`: the answer to the equasion
1. Setup the app:
    - setup venv, install requirements from ./requirements.txt, enter venv:
        ```bash
        python -m venv .venv
        source .venv/bin/activate  # on Windows use `.venv\Scripts\activate`
        pip install -r requirements.txt
        ```

2. Run the app:
    - Enter the venv environment if not already in it.
    - Run the streamlit app:
        `streamlit run src/main.py`

3. The frontend will be opened in new browser tab. From now on you are on your own :)

## Development

TODOS:
- [x] Cope with everything written in rush
- [x] Multiple cathegories support
- [x] Interactive streamlit frontend
- [x] Question type support
- [ ] CSV
- [ ] Multiple columns support (buttons -> checkboxes?)
- [ ] Error handling
- [ ] UI enchancements
- [ ] Choosing table from the frontend
- [ ] Bin?

`- ostap4ello, 2025`
