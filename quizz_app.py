import streamlit as st
import json
import random

# Load questions with caching
@st.cache_data
def load_questions():
    with open("quiz.json") as f:
        questions = json.load(f)
        random.shuffle(questions)
        return questions

# Initialize session state properly
def initialize_session_state():
    st.session_state.questions = load_questions()[:st.session_state.get("no_of_questions", 10)]
    st.session_state.current_question = 0
    st.session_state.done_question = set()  # Use a set to prevent duplicates
    st.session_state.score = 0
    st.session_state.options = {}  # Store shuffled options per question

# Initialize session state only if not set
if "questions" not in st.session_state:
    initialize_session_state()

def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("https://img.freepik.com/free-vector/question-mark-sign-glowing-digital-style-background_1017-23982.jpg?t=st=1743022772~exp=1743026372~hmac=4308750117d5b43520b106b180e516a66203c738759545582d95a09a18b493ee&w=740")

# Slider for selecting the number of questions
st.slider(
    "Select the number of questions", 
    1, 50, st.session_state.get("no_of_questions", 10), 
    key="no_of_questions",
    on_change=initialize_session_state  # Correct function reference
)

def quiz_app():
    st.title("📝 Quiz App")
    st.write("Test your knowledge by answering the questions below!")

    if st.session_state.current_question < len(st.session_state.questions):
        question = st.session_state.questions[st.session_state.current_question]
        st.write(f"**Question {st.session_state.current_question + 1}:** {question['question']}")

        # Ensure options remain the same for each question
        if st.session_state.current_question not in st.session_state.options:
            shuffled_options = question["options"].copy()
            random.shuffle(shuffled_options)
            st.session_state.options[st.session_state.current_question] = shuffled_options

        options = st.session_state.options[st.session_state.current_question]

        # Display options as radio buttons
        selected_option = st.radio("Select an option:", options, key=f"question_{st.session_state.current_question}")

        # Check answer when button is clicked
        if st.button("Submit Answer"):
            if selected_option == question["answer"]:
                st.success("✅ Correct!")
                st.balloons()
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer is: {question['answer']}")

            st.session_state.done_question.add(question['question'])  # Track attempted question
            st.session_state.current_question += 1
            st.rerun()  # Move to the next question

    else:
        st.success(f"🎉 Quiz completed! Your score: {st.session_state.score}/{len(st.session_state.questions)}")
        st.balloons()
        if st.button("Restart Quiz"):
            st.session_state.clear()  # Properly reset session state
            st.rerun()  # Restart the quiz
    st.caption("Quiz app by Huzaifa Mukhtar")
# Run the quiz app
if __name__ == "__main__":
    quiz_app()
