import streamlit as st
import json
import random
import time

def load_questions():
    with open("quiz.json") as f:
        questions = json.load(f)
        random.shuffle(questions)
        return questions

def initialize_session_state():
    st.session_state.update({
        "questions": load_questions()[:st.session_state.get("no_of_questions", 10)],
        "current_question": 0,
        "score": 0,
        "options": {},
    })

if "questions" not in st.session_state:
    initialize_session_state()

st.markdown(
    """
    <style>
    .stApp {
        background: url("https://img.freepik.com/free-vector/question-mark-sign-glowing-digital-style-background_1017-23982.jpg?t=st=1743022772~exp=1743026372~hmac=4308750117d5b43520b106b180e516a66203c738759545582d95a09a18b493ee&w=740") no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.slider("Select the number of questions", 1, 50, st.session_state.get("no_of_questions", 10), key="no_of_questions", on_change=initialize_session_state)

def quiz_app():
    st.title("📝 Quiz App")
    
    if st.session_state.current_question < len(st.session_state.questions):
        question = st.session_state.questions[st.session_state.current_question]
        st.write(f"**Question {st.session_state.current_question + 1}:** {question['question']}")
        
        if st.session_state.current_question not in st.session_state.options:
            st.session_state.options[st.session_state.current_question] = random.sample(question["options"], len(question["options"]))
        
        selected_option = st.radio("Select an option:", st.session_state.options[st.session_state.current_question], key=f"q_{st.session_state.current_question}")
        
        if st.button("Submit Answer"):
            if selected_option == question["answer"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The correct answer is: {question['answer']}")
            time.sleep(2)
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.success(f"🎉 Quiz completed! Your score: {st.session_state.score}/{len(st.session_state.questions)}")
        st.balloons()

        if st.button("Restart Quiz"):
            st.session_state.clear()
            st.rerun()
    
    st.caption("Quiz app by Huzaifa Mukhtar")

if __name__ == "__main__":
    quiz_app()
