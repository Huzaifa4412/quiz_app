import streamlit as st
import random

# Basic quiz questions
quiz_questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which language is used for web development?", "options": ["Python", "Java", "JavaScript", "C++"], "answer": "JavaScript"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "answer": "William Shakespeare"},
]

st.title("Customizable Quiz App 🧠")
st.write("Test your knowledge and choose the number of questions you want!")

# User selects the number of questions
num_questions = st.slider("How many questions do you want?", 1, len(quiz_questions), 3)

# Reset session state if number of questions changes
if "num_questions" not in st.session_state or st.session_state.num_questions != num_questions:
    st.session_state.remaining_questions = random.sample(quiz_questions, num_questions)
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.num_questions = num_questions

if len(st.session_state.remaining_questions) == 0:
    st.write(f"Quiz complete! Your final score: {st.session_state.score}/{num_questions}")
    st.balloons()
    
    if st.button("Restart"):
        st.session_state.pop("remaining_questions")
        st.session_state.pop("score")
        st.session_state.pop("current_question")
        st.session_state.pop("num_questions")
        st.rerun()
    st.stop()

current_question = st.session_state.remaining_questions[st.session_state.current_question]

st.subheader(f"Question {st.session_state.current_question + 1}")
st.write(current_question['question'])

answer = st.radio("Select your answer", current_question["options"], key=f"q{st.session_state.current_question}")

if st.button("Submit"):
    if answer == current_question['answer']:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Wrong! The correct answer is: {current_question['answer']}")
    
    st.session_state.remaining_questions.pop(0)
    st.session_state.current_question = 0
    st.rerun()

st.info(f"Your current score is: {st.session_state.score}/{num_questions}")
