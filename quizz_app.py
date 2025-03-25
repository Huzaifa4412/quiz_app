import streamlit as st
import random
import time

# Quiz questions database (kept the same as your original)
quiz_questions = [
    {"question": "What is Python?", "options": ["A programming language", "A snake", "A type of coffee", "A movie"], "answer": "A programming language"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "What data type is returned by the input() function?", "options": ["int", "str", "bool", "float"], "answer": "str"},
    {"question": "How do you start a comment in Python?", "options": ["//", "--", "#", "/*"], "answer": "#"},
    {"question": "Which of these is a mutable data type?", "options": ["Tuple", "List", "String", "Int"], "answer": "List"},
    {"question": "What is the result of 3 * 2 ** 2?", "options": ["12", "9", "6", "36"], "answer": "12"},
    {"question": "Which library is used for data manipulation in Python?", "options": ["Matplotlib", "NumPy", "Pandas", "Scikit-learn"], "answer": "Pandas"},
    {"question": "What does 'len()' do?", "options": ["Returns the length of a string", "Returns the number of elements in a list", "Counts characters in a string", "All of the above"], "answer": "All of the above"},
    {"question": "Which statement is used to exit a loop?", "options": ["stop", "break", "exit", "return"], "answer": "break"},
    {"question": "How do you install external libraries in Python?", "options": ["python install", "pip install", "lib install", "package install"], "answer": "pip install"},

    {"question": "What is the output of print(2 == 2)?", "options": ["True", "False", "Error", "2"], "answer": "True"},
    {"question": "Which operator is used for floor division?", "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "What is a lambda function?", "options": ["Anonymous function", "Loop function", "Recursive function", "Built-in function"], "answer": "Anonymous function"},
    {"question": "How do you handle exceptions in Python?", "options": ["try-except", "if-else", "catch-throw", "raise-catch"], "answer": "try-except"},
    {"question": "What does 'pass' do?", "options": ["Skips code block", "Ends a loop", "Returns a value", "Repeats the loop"], "answer": "Skips code block"},
    {"question": "Which function is used to sort a list?", "options": ["sort()", "order()", "arrange()", "filter()"], "answer": "sort()"},
    {"question": "What is the purpose of 'del'?", "options": ["Delete an object", "Clear the console", "Reset a variable", "Close a file"], "answer": "Delete an object"},
    {"question": "Which module is used for regular expressions?", "options": ["regex", "re", "pattern", "match"], "answer": "re"},
    {"question": "What is the use of 'id()' function?", "options": ["Return object type", "Return object ID", "Return object value", "Return object length"], "answer": "Return object ID"},
    {"question": "Which method adds an item to a list?", "options": ["add()", "append()", "insert()", "extend()"], "answer": "append()"},
    {"question": "What is a set in Python?", "options": ["Ordered collection", "Mutable list", "Unordered unique elements", "Immutable sequence"], "answer": "Unordered unique elements"},
    {"question": "How do you check the type of a variable?", "options": ["getType()", "type()", "isinstance()", "typeof()"], "answer": "type()"},
    {"question": "Which function creates a sequence of numbers?", "options": ["range()", "sequence()", "list()", "enumerate()"], "answer": "range()"},
    {"question": "What does 'continue' do?", "options": ["Exit the loop", "Skip current iteration", "Repeat the loop", "Break the loop"], "answer": "Skip current iteration"},
    {"question": "How do you copy a dictionary?", "options": ["copy()", "clone()", "duplicate()", "dict()"], "answer": "copy()"},
    {"question": "What is 'None' in Python?", "options": ["Empty string", "False value", "Null value", "Zero"], "answer": "Null value"},

    {"question": "What does the 'in' keyword do in Python?", "options": ["Checks membership in a sequence", "Creates a list", "Starts a loop", "Ends a function"], "answer": "Checks membership in a sequence"},
    {"question": "Which built-in function returns a sorted list?", "options": ["sort()", "sorted()", "order()", "arrange()"], "answer": "sorted()"},
    {"question": "What is the purpose of the 'enumerate()' function?", "options": ["To iterate over a sequence with index", "To sort a list", "To reverse a list", "To filter a list"], "answer": "To iterate over a sequence with index"},
    {"question": "Which operator is used to concatenate strings in Python?", "options": ["+", "&", "&&", "*"], "answer": "+"},
    {"question": "What is a list comprehension?", "options": ["A concise way to create lists", "A type of function", "A loop", "A conditional statement"], "answer": "A concise way to create lists"},
    {"question": "Which keyword is used to create an anonymous function?", "options": ["def", "lambda", "func", "anonymous"], "answer": "lambda"},
    {"question": "What does the 'strip()' method do?", "options": ["Removes whitespace from the beginning and end of a string", "Splits a string", "Replaces characters", "Converts string to lowercase"], "answer": "Removes whitespace from the beginning and end of a string"},
    {"question": "How do you convert a list into a tuple?", "options": ["tuple(list)", "list(tuple)", "convert(list)", "tupleify(list)"], "answer": "tuple(list)"},
    {"question": "Which method is used to add multiple items to the end of a list?", "options": ["append()", "extend()", "insert()", "add()"], "answer": "extend()"},
    {"question": "What is the output of print(bool(''))?", "options": ["True", "False", "Error", "None"], "answer": "False"},
    {"question": "Which keyword is used for function documentation?", "options": ["comment", "doc", "triple quotes", "None"], "answer": "triple quotes"},
    {"question": "How do you check if a key exists in a dictionary?", "options": ["if key in dict", "if dict.has_key(key)", "if key exists dict", "if dict contains key"], "answer": "if key in dict"},
    {"question": "Which method returns the keys of a dictionary?", "options": ["keys()", "values()", "items()", "all()"], "answer": "keys()"},
    {"question": "What is the output of print(type(123))?", "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"], "answer": "<class 'int'>"},
    {"question": "Which function returns a new sorted list from the items in an iterable?", "options": ["sort()", "sorted()", "order()", "listsort()"], "answer": "sorted()"},
    {"question": "What is the difference between '==' and 'is'?", "options": ["No difference", "'==' compares values; 'is' compares identities", "'==' compares identities; 'is' compares values", "'==' is for numbers and 'is' is for strings"], "answer": "'==' compares values; 'is' compares identities"},
    {"question": "What does the 'open()' function do in Python?", "options": ["Opens a file", "Closes a file", "Reads input from a file", "Creates a new file"], "answer": "Opens a file"},
    {"question": "How do you write a for loop that iterates over a list called 'items'?", "options": ["for item in items:", "for items in item:", "for i = 0; i < len(items); i++:", "for each item in items:"], "answer": "for item in items:"},
    {"question": "Which keyword is used to return a value from a function?", "options": ["yield", "return", "break", "continue"], "answer": "return"},
    {"question": "What does the 'zip()' function do?", "options": ["Combines elements from multiple iterables", "Splits a string", "Creates a list", "Sorts a list"], "answer": "Combines elements from multiple iterables"},
    {"question": "What is the purpose of the 'global' keyword?", "options": ["To create a global variable", "To access a variable defined outside a function", "To declare a variable inside a function", "To end a function"], "answer": "To access a variable defined outside a function"},
    {"question": "Which function can be used to convert a string to a float?", "options": ["str()", "int()", "float()", "bool()"], "answer": "float()"},
    {"question": "What does the 'enumerate()' function return?", "options": ["A tuple containing index and value", "A list of indices", "A dictionary", "A set"], "answer": "A tuple containing index and value"},
    {"question": "How do you define a main block in Python?", "options": ["if __name__ == '__main__':", "if main():", "def main():", "main()"], "answer": "if __name__ == '__main__':"}
]


def initialize_session_state(no_of_q):
    """Initialize session state variables based on slider selection"""
    # Clear previous session state to reset quiz
    st.session_state.clear()
    
    # Set up new session state
    st.session_state.asked_questions = []
    st.session_state.score = 0
    st.session_state.total_questions = no_of_q
    st.session_state.current_question = None
    st.session_state.quiz_started = True

def generate_unique_quiz(quiz_questions, total_questions):
    """Generate a unique set of questions based on total questions"""
    # Shuffle the entire question bank
    available_questions = random.sample(quiz_questions, min(total_questions, len(quiz_questions)))
    return available_questions

def main():
    st.title("📝 Python Quiz App")

    # Slider to select number of questions with default and max
    no_of_q = st.slider(
        "Select how many questions you want to attempt", 
        min_value=1, 
        max_value=len(quiz_questions), 
        value=min(10, len(quiz_questions))
    )

    # Button to start or restart the quiz
    if 'quiz_started' not in st.session_state or not st.session_state.quiz_started:
        if st.button("Start Quiz"):
            # Initialize session state with selected number of questions
            initialize_session_state(no_of_q)
            
            # Generate a unique set of questions
            st.session_state.quiz_questions = generate_unique_quiz(quiz_questions, no_of_q)
            st.session_state.current_question_index = 0

    # Quiz is in progress
    if 'quiz_questions' in st.session_state and st.session_state.current_question_index < len(st.session_state.quiz_questions):
        # Get current question
        current_question = st.session_state.quiz_questions[st.session_state.current_question_index]
        
        # Display question
        st.subheader(f"{current_question['question']}")
        
        # Select answer
        select_ans = st.radio(
            "Select Answer", 
            options=current_question["options"],
            key=f"question_{st.session_state.current_question_index}"
        )

        # Submit button
        if st.button("Submit Answer"):
            # Check answer
            if select_ans == current_question["answer"]:
                st.success("✅ Correct")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! The Correct Answer is: {current_question['answer']}")
            
            # Move to next question
            st.session_state.current_question_index += 1

    # Quiz completion
    elif 'quiz_questions' in st.session_state and st.session_state.current_question_index >= len(st.session_state.quiz_questions):
        st.info("Quiz Completed")   
        st.write(f"Your Score: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
        
        # Performance analysis
        percentage = (st.session_state.score / len(st.session_state.quiz_questions)) * 100
        
        if percentage == 100:
            st.balloons()
            st.success("Perfect Score! 🏆")
        elif percentage >= 70:
            st.success("Great Job! 👍")
        elif percentage >= 50:
            st.warning("Good Attempt! 📚")
        else:
            st.error("Keep Practicing! 💪")
        
        # Reset quiz
        if st.button("Start New Quiz"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()