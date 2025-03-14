import streamlit as st
import random

# Basic quiz questions
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


st.title("Customizable Quiz App 🧠")
st.write("Test your knowledge and choose the number of questions you want!")

# User selects the number of questions
num_questions = st.slider("How many questions do you want?", 1, len(quiz_questions), 20)

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
